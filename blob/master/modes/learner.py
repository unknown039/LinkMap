import os
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy

from blob.master.data_manager import BLOB_DIR
from blob.master.modes.editor import MultipleChoice, ShortResponse
from functools import cache
from random import shuffle
from string import ascii_uppercase
from torch import no_grad, softmax

from blob.master.exception_classes import ReturnToBeginning

@cache
def load_model_silently(model1_name=str(BLOB_DIR / "resources" / "models" / "sentence_transformer"),
                        model2_name=str(BLOB_DIR / "resources" / "models" / "deberta")):
    """
    Loads the sentence embedding model used for semantic
    similarity comparisons between user text and stored text.
    Suppresses startup output and requires local cache.
    """
    print(f"Loading Sentence Transformer model: all-MiniLM-L6-v2")
    print(f"Loading Natural Language Inference model: DeBERTa-v3-base-mnli-fever-anli")
    print(f"This may take 10-30 seconds.\n")

    # MUST run before importing transformers/torch/sentence_transformers
    from os import environ
    environ["TRANSFORMERS_OFFLINE"] = "1"
    environ["HF_DATASETS_OFFLINE"] = "1"
    environ["HF_HUB_OFFLINE"] = "1"
    environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
    environ["TORCH_CPP_LOG_LEVEL"] = "0"
    environ["PYTHONWARNINGS"] = "ignore"

    # minimal logging/warning suppression
    from warnings import filterwarnings
    filterwarnings("ignore")

    from transformers import logging as transformers_logging
    transformers_logging.set_verbosity_error()

    from logging import getLogger, ERROR
    getLogger("transformers").setLevel(ERROR)
    getLogger("huggingface_hub").setLevel(ERROR)
    getLogger("torch").setLevel(ERROR)

    # redirect both stdout and stderr to devnull while loading
    with open(os.devnull, "w") as devnull, redirect_stdout(devnull), redirect_stderr(devnull):
        from sentence_transformers import SentenceTransformer
        from transformers import AutoTokenizer, AutoModelForSequenceClassification

        emb_model1 = SentenceTransformer(model1_name, local_files_only=True)  # local_files_only=True ensures no hub contact
        # noinspection PyNoneFunctionAssignment
        tokenizer1 = AutoTokenizer.from_pretrained(model2_name, local_files_only=True)
        nli_model1 = AutoModelForSequenceClassification.from_pretrained(model2_name, local_files_only=True)
    from sentence_transformers.util import cos_sim

    return emb_model1, cos_sim, nli_model1, tokenizer1

def get_sim_score(sentence1: str, sentence2: str):
    emb_model, cos_sim, nli_model, tokenizer = load_model_silently()

    return cos_sim(emb_model.encode(sentence1.strip(), convert_to_tensor=True),
            emb_model.encode(sentence2.strip(), convert_to_tensor=True)).item()

def get_nli_scores(sentence1: str, sentence2: str):
    emb_model, cos_sim, nli_model, tokenizer = load_model_silently()

    # noinspection PyCallingNonCallable
    inputs = tokenizer(
        sentence1,
        sentence2,
        return_tensors="pt",
        truncation=True
    )

    with no_grad():
        logits = nli_model(**inputs).logits
    probs = softmax(logits, dim=1)[0]
    labels = nli_model.config.id2label

    return {
        labels[i]: float(probs[i])
        for i in range(len(probs))
    }

# Global variables
alphabet = ascii_uppercase

class Learner:
    def __init__(self, data, save):
        self.data = data
        self.save = save
        self.subject_prompt = "Subject: "
        self.quiz_prompt = "Quiz: "
        self.instant_feedback_prompt = "Instant Feedback: "
        self.instant_feedback = None
        load_model_silently()

    def learner_mode(self):
        while True:
            subject = self.get_subject_name()
            quiz = self.get_quiz_name(subject)
            self.instant_feedback = self.get_instant_feedback()

            print()

            if not self.data[subject][quiz]:
                print(f"Quiz is empty\n")
                continue

            self.quiz_mode(self.data[subject][quiz].values())

    def quiz_mode(self, quiz):
        quiz = deepcopy(list(quiz))
        shuffle(quiz)
        score = 0
        total_score = 0

        for question_index in range(len(quiz)):
            question = quiz[question_index]

            print(f"{question_index + 1}. ", end="")

            match type(question).__name__:
                case "MultipleChoice":
                    score += self.mc(question)
                case "ShortResponse":
                    score += self.sr(question)
                case _:
                    raise TypeError("Invalid question type")

            total_score += question.points_worth
            print()

        print(f"Score: {score:.2g}/{total_score:g} | {score/total_score*100:.2f}%\n")

    def mc(self, mc_question=MultipleChoice):
        correct_answer = None
        print(mc_question.prompt)
        shuffle(mc_question.answers_list)

        for i in range(len(mc_question.answers_list)):
            print(f"{alphabet[i]}. {mc_question.answers_list[i]}")

            if mc_question.answers_list[i] == mc_question.correct_answer:
                correct_answer = alphabet[i]

        learner_answer = input("\nAnswer: ").strip().upper()

        if correct_answer is None:
            raise Exception("Correct answer never got assigned to an alphabet")

        self.print_instant_feedback(learner_answer == correct_answer, correct_answer)

        return mc_question.points_worth if learner_answer == correct_answer else 0

    def sr(self, sr_question=ShortResponse):
        print(f"{sr_question.prompt}")
        learner_answer = input("Answer: ").strip()

        if not sr_question.partial_credit:
            self.print_instant_feedback(sr_question.correct_answer == learner_answer, sr_question.correct_answer)

            return sr_question.points_worth if sr_question.correct_answer == learner_answer else 0

        nli_scores = get_nli_scores(learner_answer, sr_question.correct_answer)
        answer_is_incorrect = max(nli_scores["contradiction"], nli_scores["neutral"]) > 0.75 or nli_scores["entailment"] < 0.5
        self.print_instant_feedback(not answer_is_incorrect, sr_question.correct_answer)

        if answer_is_incorrect:
            return 0

        return max(0, get_sim_score(sr_question.correct_answer, learner_answer)) * sr_question.points_worth

    def get_subject_name(self):
        while True:
            subject = self.check_and_prompt(self.subject_prompt)

            if subject[0] in self.data:
                return subject[0]

            print(f"{subject[1]} does not exist\n")

    def get_quiz_name(self, subject):
        while True:
            quiz = self.check_and_prompt(self.quiz_prompt)

            if quiz[0] in self.data[subject]:
                return quiz[0]

            print(f"{quiz[1]} does not exist\n")

    def get_instant_feedback(self):
        while True:
            response = self.check_and_prompt(self.instant_feedback_prompt)

            if response[0] == "t":
                return True
            elif response[0] == "f":
                return False
            else:
                print(f"{response[1]} is not T/F\n")

    def print_instant_feedback(self, is_correct, correct_answer):
        if self.instant_feedback:
            if is_correct:
                print(f"Correct!")
            else:
                print(f"Incorrect: {correct_answer}")

    def check_and_prompt(self, prompt):
        old_response = input(prompt).strip()
        response = old_response.upper()

        if response == "STOP":
            raise SystemExit("Exiting LinkMap")
        elif response == "BACK":
            raise ReturnToBeginning()
        elif response == "SAVE":
            self.save()

        if prompt == self.subject_prompt or prompt == self.quiz_prompt or prompt == self.instant_feedback_prompt:
            return response.lower(), old_response
        return response
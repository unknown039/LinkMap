import os
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from blob.master.modes.editor import MultipleChoice, ShortResponse
from random import shuffle
from string import ascii_uppercase
from torch import no_grad, softmax

def load_model_silently(model1_name="sentence-transformers/all-MiniLM-L6-v2",
                        model2_name="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"):
    """
    Loads the sentence embedding model used for semantic
    similarity comparisons between user text and stored text.
    Suppresses startup output and requires local cache.
    """
    print(f"Loading Sentence Transformer model: {model1_name}")
    print(f"Loading Natural Language Inference model: {model2_name}")
    print(f"This may take 10-30 seconds.\n")

    # TODO: Package model with distribution

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

class ReturnToBeginning(Exception):
    pass

def get_sim_score(sentence1: str, sentence2: str):
    return cos_sim(emb_model.encode(sentence1.strip(), convert_to_tensor=True),
            emb_model.encode(sentence2.strip(), convert_to_tensor=True)).item()

def get_nli_scores(sentence1: str, sentence2: str):
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

def mc(mc_question=MultipleChoice):
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

    return mc_question.points_worth if learner_answer == correct_answer else 0

def sr(sr_question=ShortResponse):
    print(f"{sr_question.prompt}")

    if not sr_question.partial_credit:
        return sr_question.points_worth if sr_question.correct_answer == input("Answer: ").strip() else 0

    # TODO: Maybe switch to a better model
    user_answer = input("Answer: ")
    nli_scores = get_nli_scores(user_answer, sr_question.correct_answer)

    print(f"NLI Scores: {nli_scores}")

    if nli_scores["contradiction"] > 0.75 or nli_scores["neutral"] > 0.75 or nli_scores["entailment"] < 0.5:
        return 0

    return max(0, get_sim_score(sr_question.correct_answer, user_answer)) * sr_question.points_worth

emb_model, cos_sim, nli_model, tokenizer = load_model_silently()
alphabet = ascii_uppercase

class Learner:
    def __init__(self, data):
        self.data = data
        self.subject_prompt = "Subject: "
        self.quiz_prompt = "Quiz: "

    def learner_mode(self):
        while True:
            subject = self.get_subject_name()
            quiz = self.get_quiz_name(subject)
            print()

            self.quiz_mode(self.data[subject][quiz].values())

    def quiz_mode(self, quiz):
        quiz = deepcopy(list(quiz))
        shuffle(quiz)
        score = 0
        total_score = 0

        # TODO: Add feature to enable immediate feedback

        for question_index in range(len(quiz)):
            question = quiz[question_index]

            print(f"{question_index + 1}. ", end="")

            match type(question).__name__:
                case "MultipleChoice":
                    score += mc(question)
                case "ShortResponse":
                    score += sr(question)
                case _:
                    raise TypeError("Invalid question type")

            total_score += question.points_worth
            print()

        print(f"score: {score:.3g}/{total_score:g} | {score/total_score*100:.2f}%")

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

    def check_and_prompt(self, prompt):
        old_response = input(prompt).strip()
        response = old_response.upper()

        if response == "FINISHED" or response == "STOP":
            from ..main import end_learning
            end_learning()
        elif response == "BACK":
            raise ReturnToBeginning()

        if prompt == self.subject_prompt or prompt == self.quiz_prompt:
            return response.lower(), old_response
        return response
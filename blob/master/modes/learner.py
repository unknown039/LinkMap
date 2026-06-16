import os
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from blob.master.modes.editor import MultipleChoice, ShortResponse
from random import shuffle
from string import ascii_uppercase

class ReturnToBeginning(Exception):
    pass

class Learner:
    def __init__(self, data):
        self.model, self.cos_sim = load_model_silently()
        self.data = data
        self.subject_prompt = "Subject: "
        self.quiz_prompt = "Quiz: "
        self.alphabet = ascii_uppercase

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
                    score += self.mc(question)
                case "ShortResponse":
                    score += self.sr(question)
                case _:
                    raise TypeError("Invalid question type")

            total_score += question.points_worth
            print()

        print(f"score: {score:.3g}/{total_score:g} | {score/total_score*100:.2f}%")

    def mc(self, mc_question=MultipleChoice):
        correct_answer = None
        print(mc_question.prompt)
        shuffle(mc_question.answers_list)

        for i in range(len(mc_question.answers_list)):
            print(f"{self.alphabet[i]}. {mc_question.answers_list[i]}")

            if mc_question.answers_list[i] == mc_question.correct_answer:
                correct_answer = self.alphabet[i]

        learner_answer = input("\nAnswer: ").strip().upper()

        if correct_answer is None:
            raise Exception("Correct answer never got assigned to an alphabet")

        return mc_question.points_worth if learner_answer == correct_answer else 0

    def sr(self, sr_question=ShortResponse):
        print(f"{sr_question.prompt}")

        if not sr_question.partial_credit:
            return sr_question.correct_answer == input("Answer: ").strip()

        # TODO: Transformer model is not great at dealing with negation

        return max(0, self.cos_sim(self.model.encode(sr_question.correct_answer.strip(), convert_to_tensor=True),
        self.model.encode(input("Answer: ").strip(), convert_to_tensor=True)).item()) * sr_question.points_worth

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

def load_model_silently(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Loads the sentence embedding model used for semantic
    similarity comparisons between user text and stored text.
    Suppresses startup output and requires local cache.
    """
    print(f"Loading transformer model: {model_name}")
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
        model = SentenceTransformer(model_name, local_files_only=True)  # local_files_only=True ensures no hub contact
    from sentence_transformers.util import cos_sim

    return model, cos_sim
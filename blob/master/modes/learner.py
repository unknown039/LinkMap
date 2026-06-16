import os
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from random import shuffle

class ReturnToBeginning(Exception):
    pass

class Learner:
    def __init__(self, data):
        self.model = load_model_silently()
        self.data = data
        self.subject_prompt = "Subject: "
        self.quiz_prompt = "Quiz: "

    def learner_mode(self):
        while True:
            subject = self.get_subject_name()
            quiz = self.get_quiz_name(subject)

            self.quiz_mode(self.data[subject][quiz].values())

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

    def quiz_mode(self, quiz):
        quiz = deepcopy(list(quiz))
        shuffle(quiz)

        print(f"{quiz}")

def load_model_silently(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Loads the sentence embedding model used for semantic
    similarity comparisons between user text and stored text.
    Suppresses startup output and requires local cache.
    """

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
    return model
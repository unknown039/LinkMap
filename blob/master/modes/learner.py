import os
from contextlib import redirect_stdout, redirect_stderr

class ReturnToBeginning(Exception):
    pass


def check_and_prompt(prompt):
    from ..main import end_learning

    response = input(prompt).strip().upper()

    if response == "FINISHED" or response == "STOP":
        end_learning()
    elif response == "BACK":
        raise ReturnToBeginning()

    return response

class Learner:
    def __init__(self):
        self.model = load_model_silently()

    def learner_mode(self):
        pass

def load_model_silently(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Loads the sentence embedding model used for semantic
    similarity comparisons between user text and stored text.
    Suppresses startup output and requires local cache.
    """

    # redirect both stdout and stderr to devnull while loading
    with open(os.devnull, "w") as devnull, redirect_stdout(devnull), redirect_stderr(devnull):
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(model_name, local_files_only=True)  # local_files_only=True ensures no hub contact
    return model
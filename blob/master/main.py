import json
from dataclasses import asdict
from pathlib import Path

import blob.master.modes.learner as learner

import blob.master.modes.editor as editor
from blob.master.modes.editor import ReturnToBeginning, Editor, MultipleChoice, ShortResponse

# top of your script — MUST run before importing transformers/torch/sentence_transformers
import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TORCH_CPP_LOG_LEVEL"] = "0"
os.environ["PYTHONWARNINGS"] = "ignore"

# minimal logging/warning suppression
import warnings
warnings.filterwarnings("ignore")

from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()

import logging
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)


data_file_path = Path(__file__).parent.parent/"resource"/"data.json"
test_data_file_path = Path(__file__).parent.parent / "resource" / "test_data.json"

with open(data_file_path, "r") as f:
    data = json.load(f)

with open(test_data_file_path, "r") as f1:
    test_data = json.load(f1)

def serialize_data(data_to_serialize: dict):
    for subject_name, quizzes in data_to_serialize.items():
        for quiz_name, question in quizzes.items():
            for question_number, question_content in question.items():
                data_to_serialize[subject_name][quiz_name][question_number] = asdict(question_content)

    return data_to_serialize

def deserialize_test_data():
    question_types = {
        "MC": MultipleChoice,
        "SR": ShortResponse
    }

    def deserialize_question(dataclass: dict):
        try:
            return question_types[dataclass["type"]](**dataclass)
        except KeyError:
            raise ValueError(f"Unknown question type: {dataclass.get('type')}")

    for subject, quizzes in test_data.items():
        for quiz, question in quizzes.items():
            for question_number, question_content in question.items():
                test_data[subject][quiz][question_number] = deserialize_question(question_content)

def end():
    print(json.dumps(data, indent=4))
    print("File is overwritten")
    with open (data_file_path, "w") as f2:
        f2.write(json.dumps(data, indent=4))

    global test_data
    test_data = serialize_data(test_data)
    print(json.dumps(test_data, indent=4))
    print("Test data is overwritten")
    with open(test_data_file_path, "w") as f2:
        f2.write(json.dumps(test_data, indent=4))

    raise SystemExit("Exiting LinkMap")

def end_learning():
    raise SystemExit("Exiting LinkMap")

if __name__ == "__main__":
    deserialize_test_data()

    while True:
        try:
            role = input("Are you editing or learning? (E/L) ").lower().strip()
            print()

            if role == "e":
                edit = Editor(test_data, end)
                edit.editor_mode()
            elif role == "l":
                pass
            elif role == "stop":
                end_learning()
            elif role == "finished":
                end()
        except ReturnToBeginning:
            pass
import sys
from copy import deepcopy
from dataclasses import asdict, is_dataclass
from blob.master.modes.editor import MultipleChoice, ShortResponse
from json import dumps, load
from pathlib import Path

from blob.master.exception_classes import ReturnToBeginning

def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)

def serialize_data(memory_data: dict):
    data_to_serialize = deepcopy(memory_data)

    for subject_name, quizzes in data_to_serialize.items():
        for quiz_name, question in quizzes.items():
            for question_number, question_content in question.items():
                if is_dataclass_instance(question_content):
                    data_to_serialize[subject_name][quiz_name][question_number] = asdict(question_content)

    return data_to_serialize

QUESTION_TYPES = {
    "MC": MultipleChoice,
    "SR": ShortResponse
}

def deserialize_test_data():
    def deserialize_question(dataclass: dict):
        try:
            return QUESTION_TYPES[dataclass["type"]](**{k: v for k, v in dataclass.items() if k != "type"})
        except KeyError:
            raise ValueError(f"Unknown question type: {dataclass.get('type')}")

    for subject, quizzes in data.items():
        for quiz, question in quizzes.items():
            for question_number, question_content in question.items():
                if isinstance(question_content, dict):
                    data[subject][quiz][question_number] = deserialize_question(question_content)

    return data

def save():
    global data
    serialized_data = serialize_data(deepcopy(data))
    with open(data_file_path, "w") as f2:
        f2.write(dumps(serialized_data, indent=4))

    print(f"Successfully saved data to {data_file_path}\n")
    raise ReturnToBeginning()

if getattr(sys, 'frozen', False):
    BLOB_DIR = Path(sys.executable).parent
else:
    BLOB_DIR = Path(__file__).parent.parent

data_file_path = BLOB_DIR / "resources" / "data.json"

if not data_file_path.exists():
    data_file_path.parent.mkdir(parents=True, exist_ok=True)
    data_file_path.write_text("{}", encoding="utf-8")

with data_file_path.open("r", encoding="utf-8") as f:
    data = load(f)

deserialize_test_data()
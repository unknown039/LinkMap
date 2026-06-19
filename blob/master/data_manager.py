from dataclasses import asdict
from blob.master.modes.editor import ReturnToBeginning, MultipleChoice, ShortResponse
from json import dumps, load
from pathlib import Path

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
            return question_types[dataclass["type"]](**{k: v for k, v in dataclass.items() if k != "type"})
        except KeyError:
            raise ValueError(f"Unknown question type: {dataclass.get('type')}")

    for subject, quizzes in data.items():
        for quiz, question in quizzes.items():
            for question_number, question_content in question.items():
                data[subject][quiz][question_number] = deserialize_question(question_content)

def save():
    global data
    data = serialize_data(data)
    with open(data_file_path, "w") as f2:
        f2.write(dumps(data, indent=4))

    print(f"Successfully saved data to {data_file_path}\n")
    raise ReturnToBeginning()

data_file_path = Path(__file__).parent.parent / "resource" / "data.json"

with open(data_file_path, "r") as f1:
    data = load(f1)

deserialize_test_data()
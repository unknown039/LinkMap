import json
from dataclasses import asdict
from pathlib import Path

import blob.master.modes.learner as learner
from blob.master.modes.editor import ReturnToBeginning, Editor, MultipleChoice, ShortResponse

data_file_path = Path(__file__).parent.parent / "resource" / "data.json"

with open(data_file_path, "r") as f1:
    data = json.load(f1)

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

def end():
    global data
    data = serialize_data(data)
    print(json.dumps(data, indent=4))
    print("Test data is overwritten")
    with open(data_file_path, "w") as f2:
        f2.write(json.dumps(data, indent=4))

    raise SystemExit("Exiting LinkMap")

def end_learning():
    raise SystemExit("Exiting LinkMap")

if __name__ == "__main__":
    deserialize_test_data()

    while True:
        try:
            role = input("Editor/Learner: ").lower().strip()
            print()

            if role == "e":
                edit = Editor(data, end)
                edit.editor_mode()
            elif role == "l":
                learn = learner.Learner(data)
                learn.learner_mode()
            elif role == "stop":
                end_learning()
            elif role == "finished":
                end()
            else:
                print(f'{role} is not "E" or "L"')
        except ReturnToBeginning:
            pass
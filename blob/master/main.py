import json
from pathlib import Path

import blob.master.modes.learner as learner

import blob.master.modes.editor as editor
from blob.master.modes.editor import ReturnToBeginning

data_file_path = Path(__file__).parent.parent/"resource"/"data.json"

with open(data_file_path, "r") as f:
    data = json.load(f)

def end():
    print(json.dumps(data, indent=4))
    print("File is overwritten")
    with open (data_file_path, "w") as f:
        f.write(json.dumps(data, indent=4))
    raise SystemExit("Exiting LinkMap")

def end_learning():
    raise SystemExit("Exiting LinkMap")

if __name__ == "__main__":
    print("Type STOP at any moment to end the program")

    while True:
        try:
            role = input("Are you editing or learning? (E/L) ").lower().strip()
            print()

            if role == "e":
                editor.editor_mode(data, end)
            elif role == "l":
                learner.learner_mode(data)
            elif role == "stop":
                end_learning()
            elif role == "finished":
                end()
        except ReturnToBeginning:
            role = input("Are you editing or learning? (E/L) ").lower().strip()
            print()

            if role == "e":
                editor.editor_mode(data, end)
            elif role == "l":
                learner.learner_mode(data)
            elif role == "finished":
                end()
            elif role == "stop":
                end_learning()
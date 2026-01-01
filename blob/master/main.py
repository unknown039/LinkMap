import json
from pathlib import Path

import blob.master.modes.editor as editor

with open(Path(__file__).parent.parent/"resource"/"data.json", "r") as f:
    data = json.load(f)

def end():
    print(data)
    raise SystemExit("Exiting LinkMap")

def learner_mode():
    print(f"Temp")

if __name__ == "__main__":
    print("Type STOP at any moment to end the program")

    while True:
        role = input("Are you editing or learning? (E/L) ").lower().strip()
        print()

        if role == "e":
            editor.editor_mode(data, end)
        elif role == "l":
            learner_mode()
        elif role == "stop":
            end()
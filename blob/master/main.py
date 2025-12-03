import json
from pathlib import Path

with open(Path(__file__).parent.parent/"resource"/"data.json", "r") as f:
    data = json.load(f)

def end():
    print(data)
    raise SystemExit("Exiting LinkMap")

def editor_mode():
    print("Type FINISHED at any moment to save your changes. "
          "\nSTOP would end the program and discard your changes."
          "\nBACK would take you back to the beginning page (a.k.a the one that asks what would you like to do).\n")
    subject_level = input("Would you like to add a new subject or proceed to an existing subject? (A/P) ").lower().strip()
    subject = input("Subject: ").lower().strip()

    if subject_level == "a":
        data[subject] = None
    elif subject_level == "finished" or subject_level == "back":
        return
    elif subject_level == "stop":
        end()
    elif subject_level == "p" and data[subject] is None:
        print("That subject does not exist.")

    quiz = input("What quiz would you like to add? ")

    if quiz == "STOP":
        end()
    elif quiz == "BACK":
        return
    elif quiz == "FINISHED":
        data[subject][quiz] = None


def learner_mode():
    print(f"Temp")

if __name__ == "__main__":
    while True:
        print("Type STOP at any moment to end the program")
        role = input("Are you editing or learning? (E/L) ").lower().strip()
        print()

        if role == "e":
            editor_mode()
        elif role == "l":
            learner_mode()
        elif role == "stop":
            end()
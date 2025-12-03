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

    quiz = input("What quiz would you like to add? ").lower().strip()

    if quiz == "stop":
        end()
    elif quiz == "back":
        return
    elif quiz == "finished":
        data[subject][quiz] = None

    num_of_elements = None

    while True:
        num_of_elements = input("How many entries would you like to have in this quiz? ")

        try:
            num_of_elements = int(num_of_elements)
        except ValueError:
            print("You must enter a positive integer. Try again\n")
            continue

        if num_of_elements <= 0:
            print("You must enter a positive integer. Try again\n")
        else:
            break


def learner_mode():
    print(f"Temp")

if __name__ == "__main__":
    print("Type STOP at any moment to end the program")

    while True:
        role = input("Are you editing or learning? (E/L) ").lower().strip()
        print()

        if role == "e":
            editor_mode()
        elif role == "l":
            learner_mode()
        elif role == "stop":
            end()
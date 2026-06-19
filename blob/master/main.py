import blob.master.modes.learner as learner
from blob.master.modes.editor import ReturnToBeginning, Editor
from data_manager import data, save

if __name__ == "__main__":
    while True:
        try:
            role = input("Editor/Learner: ").lower().strip()
            print()

            if role == "e":
                edit = Editor(data, save)
                edit.editor_mode()
            elif role == "l":
                learn = learner.Learner(data, save)
                learn.learner_mode()
            elif role == "stop":
                raise SystemExit("Exiting LinkMap")
            elif role == "save":
                save()
            else:
                print(f'{role} is not "E" or "L"')
        except ReturnToBeginning:
            pass
from blob.master.exception_classes import ReturnToBeginning
from blob.master.modes.learner import Learner
from blob.master.modes.editor import Editor
from blob.master.data_manager import save, data

if __name__ == "__main__":
    while True:
        try:
            inputted_role = input("Editor/Learner: ")
            role = inputted_role.lower().strip()
            print()

            if role == "e":
                edit = Editor(data, save)
                edit.editor_mode()
            elif role == "l":
                learn = Learner(data, save)
                learn.learner_mode()
            elif role == "stop":
                raise SystemExit("Exiting LinkMap")
            elif role == "save":
                save()
            else:
                print(f'"{inputted_role}" is not "E" or "L"')
        except ReturnToBeginning:
            pass
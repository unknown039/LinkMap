import json
from pathlib import Path

import blob.master.modes.learner as learner

import blob.master.modes.editor as editor
from blob.master.modes.editor import ReturnToBeginning, EditorMode

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
test_data_file_path = Path(__file__).parent.parent/"resource"/"test_data.json"

with open(data_file_path, "r") as f:
    data = json.load(f)

with open(test_data_file_path, "r") as f:
    test_data = json.load(f)

def end():
    print(json.dumps(data, indent=4))
    print("File is overwritten")
    with open (data_file_path, "w") as f1:
        f1.write(json.dumps(data, indent=4))

    print(json.dumps(test_data, indent=4))
    print("Test data is overwritten")
    with open(test_data_file_path, "w") as f2:
        f2.write(json.dumps(test_data, indent=4))

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
                edit = EditorMode(test_data, end)
                edit.editor_mode_test()
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
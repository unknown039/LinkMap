import random
import time

ELEMENTS = [
    {"name": "Hydrogen", "symbol": "H", "number": 1},
    {"name": "Helium", "symbol": "He", "number": 2},
    {"name": "Lithium", "symbol": "Li", "number": 3},
    {"name": "Beryllium", "symbol": "Be", "number": 4},
    {"name": "Boron", "symbol": "B", "number": 5},
    {"name": "Carbon", "symbol": "C", "number": 6},
    {"name": "Nitrogen", "symbol": "N", "number": 7},
    {"name": "Oxygen", "symbol": "O", "number": 8},
    {"name": "Fluorine", "symbol": "F", "number": 9},
    {"name": "Neon", "symbol": "Ne", "number": 10},
    {"name": "Sodium", "symbol": "Na", "number": 11},
    {"name": "Magnesium", "symbol": "Mg", "number": 12},
    {"name": "Aluminium", "symbol": "Al", "number": 13},
    {"name": "Silicon", "symbol": "Si", "number": 14},
    {"name": "Phosphorus", "symbol": "P", "number": 15},
    {"name": "Sulfur", "symbol": "S", "number": 16},
    {"name": "Chlorine", "symbol": "Cl", "number": 17},
    {"name": "Argon", "symbol": "Ar", "number": 18},
    {"name": "Potassium", "symbol": "K", "number": 19},
    {"name": "Calcium", "symbol": "Ca", "number": 20},
    {"name": "Scandium", "symbol": "Sc", "number": 21},
    {"name": "Titanium", "symbol": "Ti", "number": 22},
    {"name": "Vanadium", "symbol": "V", "number": 23},
    {"name": "Chromium", "symbol": "Cr", "number": 24},
    {"name": "Manganese", "symbol": "Mn", "number": 25},
    {"name": "Iron", "symbol": "Fe", "number": 26},
    {"name": "Cobalt", "symbol": "Co", "number": 27},
    {"name": "Nickel", "symbol": "Ni", "number": 28},
    {"name": "Copper", "symbol": "Cu", "number": 29},
    {"name": "Zinc", "symbol": "Zn", "number": 30},
    {"name": "Gallium", "symbol": "Ga", "number": 31},
    {"name": "Germanium", "symbol": "Ge", "number": 32},
    {"name": "Arsenic", "symbol": "As", "number": 33},
    {"name": "Selenium", "symbol": "Se", "number": 34},
    {"name": "Bromine", "symbol": "Br", "number": 35},
    {"name": "Krypton", "symbol": "Kr", "number": 36},
    {"name": "Rubidium", "symbol": "Rb", "number": 37},
    {"name": "Strontium", "symbol": "Sr", "number": 38},
    {"name": "Yttrium", "symbol": "Y", "number": 39},
    {"name": "Zirconium", "symbol": "Zr", "number": 40},
    {"name": "Niobium", "symbol": "Nb", "number": 41},
    {"name": "Molybdenum", "symbol": "Mo", "number": 42},
    {"name": "Technetium", "symbol": "Tc", "number": 43},
    {"name": "Ruthenium", "symbol": "Ru", "number": 44},
    {"name": "Rhodium", "symbol": "Rh", "number": 45},
    {"name": "Palladium", "symbol": "Pd", "number": 46},
    {"name": "Silver", "symbol": "Ag", "number": 47},
    {"name": "Cadmium", "symbol": "Cd", "number": 48},
    {"name": "Indium", "symbol": "In", "number": 49},
    {"name": "Tin", "symbol": "Sn", "number": 50},
]



def evaluate_answer(user_text, correct):
    user_tokens = [t.strip().lower() for t in user_text.split() if t.strip()]
    correct_tokens = [str(t).strip().lower() for t in correct]
    return sorted(user_tokens) == sorted(correct_tokens)


def format_correct(correct):
    return " ".join(map(str, correct))


def start_quiz():
    modes = ["random", "number", "name", "symbol"]
    print("Modes:")
    print("- random: cycles between number → name → symbol")
    print("- number / name / symbol: prompt is that field; provide the other two")
    print(f"Elements available: {len(ELEMENTS)}")

    while True:
        mode = input(f"Choose a mode ({', '.join(modes)}): ").strip().lower()
        if mode in modes:
            break
        print("Invalid mode, try again.")

    elements = ELEMENTS.copy()
    random.shuffle(elements)
    score = 0
    start_time = time.time()

    for idx, elem in enumerate(elements):
        if mode == "random":
            qtype = idx % 3
            if qtype == 0:
                prompt_text = f"{elem['number']}: "
                correct = [elem["name"], elem["symbol"]]
            elif qtype == 1:
                prompt_text = f"{elem['name']}: "
                correct = [elem["symbol"], str(elem["number"])]
            else:
                prompt_text = f"{elem['symbol']}: "
                correct = [elem["name"], str(elem["number"])]
        else:
            prompt_text = f"{elem[mode]}: "
            correct = [str(elem["name"]), str(elem["symbol"]), str(elem["number"])]
            correct.remove(str(elem[mode]))

        while True:
            user_input = input(
                f"Q{idx + 1}/{len(elements)} ({mode}) | Score: {score} | Elapsed: {time.time() - start_time:.1f}s\n{prompt_text}")
            if user_input.strip().upper() == "STOP":
                print("\nQuiz stopped by user.")
                duration = time.time() - start_time
                print(f"Final score: {score} / {idx}")
                print(f"Total time: {duration:.2f} seconds")
                return
            if not user_input.strip():
                print("Empty answer — please type something or 'STOP' to quit.")
                continue
            if evaluate_answer(user_input, correct):
                print("Correct!\n")
                score += 1
            else:
                print(f"wrong. Correct answer: {format_correct(correct)}\n")
            break

    duration = time.time() - start_time
    print("Quiz finished!")
    print(f"Final score: {score} / {len(elements)}")
    print(f"Total time: {duration:.2f} seconds")

    replay = input("Do you want to keep practicing? (yes/no): ").lower()
    if replay not in ("yes", "y"):
        print("Thanks for playing! Goodbye.")
        return
    else:
        print()
        start_quiz()


if __name__ == "__main__":
    print("Welcome to the Periodic Table Quiz!")
    print("Type 'STOP' anytime to quit.\n")
    start_quiz()
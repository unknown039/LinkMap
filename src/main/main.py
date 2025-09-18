import random

# Basic periodic table data
elements = [
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
    {"name": "Aluminum", "symbol": "Al", "number": 13},
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
    {"name": "Zinc", "symbol": "Zn", "number": 30}
]


def quiz():
    score = 0
    current_question = 0
    random.shuffle(elements)

    for elem in elements:
        q_type = random.choice(["name", "symbol", "number"])

        if q_type == "name":
            answer = input(f"What is the name and symbol of element #{elem['number']}? ").strip().split()
            correct = [elem['name'], elem['symbol']]
        elif q_type == "symbol":
            answer = input(f"What is the atomic number and symbol for {elem['name']}? ").strip().split()
            correct = [elem['symbol'], str(elem['number'])]
        else:  # number
            answer = input(f"What is the atomic number and symbol of {elem['name']}? ").strip().split()
            correct = [elem['symbol'], str(elem['number'])]

        if sorted(answer) == sorted(correct):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct}.\n")
        current_question += 1
        print(f"{score}/{current_question}")

    print(f"Quiz finished! Your score: {score}/{len(elements)}")


if __name__ == "__main__":
    quiz()
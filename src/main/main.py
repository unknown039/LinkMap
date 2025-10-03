import random
import time
import streamlit as st

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
    {"name": "Zirconium", "symbol": "Zr", "number": 40}
]
st.title("Periodic Table Quiz")


def quiz():
    score = 0
    current_question = 0
    random.shuffle(elements)
    st.write(f"Quiz over Elements 1-{len(elements)}! Type STOP At anytime to exit.")

    while True:
        current_mode = st.text_input('Would you like to do random mode or number/symbol/name only mode? ')
        if current_mode == 'random':
            start_time = time.time()
            for elem in elements:

                if current_question % 3 == 0: #number
                    answer = st.text_input(f"{elem['number']} ").strip().split()
                    correct = [elem['name'], elem['symbol']]
                elif current_question % 3 == 1: #name
                    answer = st.text_input(f"{elem['name']} ").strip().split()
                    correct = [elem['symbol'], str(elem['number'])]
                else:  #symbol
                    answer = st.text_input(f"{elem['symbol']} ").strip().split()
                    correct = [elem['name'], str(elem['number'])]

                if answer[0] == 'STOP':
                    exit()

                if sorted(answer) == sorted(correct):
                    st.write("Correct!\n")
                    score += 1
                else:
                    st.write(f"Wrong. The correct answer is {' '.join(correct)}.\n")
                current_question += 1
                st.write(f"{score}/{current_question}")
            st.write(f"Quiz finished! Your score: {score}/{len(elements)}")
            st.write(f"You finished the quiz in: {(time.time() - start_time):.2f} seconds!")
            if st.text_input("Would you like to continue?").lower() == 'no':
                exit()
            else:
                st.write()
            score = 0
            current_question = 0
            random.shuffle(elements)
        else:
            non_random_mode(current_mode)

def non_random_mode(mode):
    score = 0
    current_question = 0
    start_time = time.time()
    for elem in elements:
        answer = st.text_input(f"{elem[mode]} ").strip().split()
        correct = [str(elem['name']), str(elem['symbol']), str(elem['number'])]
        correct.remove(str(elem[mode]))

        if answer[0] == 'STOP':
            exit()

        if sorted(answer) == sorted(correct):
            st.write("Correct!\n")
            score += 1
        else:
            st.write(answer)
            st.write(f"Wrong. The correct answer is {' '.join(correct)}.\n")
        current_question += 1
        st.write(f"{score}/{current_question}")
    st.write(f"Quiz finished! Your score: {score}/{len(elements)}")
    st.write(f"You finished the quiz in: {(time.time() - start_time):.2f} seconds!")
    if st.text_input("Would you like to continue? ") == 'STOP':
        exit()
    else:
        st.write()

if __name__ == "__main__":
    quiz()
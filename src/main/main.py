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
]

st.title("Periodic Table Quiz")

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "elements" not in st.session_state:
    st.session_state.elements = elements.copy()
    random.shuffle(st.session_state.elements)

# Stop the quiz
if st.button("STOP"):
    st.write(f"Quiz stopped. Your score: {st.session_state.score}/{st.session_state.current_question}")
    st.stop()

# Determine the current element
if st.session_state.current_question < len(st.session_state.elements):
    elem = st.session_state.elements[st.session_state.current_question]

    # Decide mode (rotate: number, name, symbol)
    mode_cycle = ["number", "name", "symbol"]
    mode = mode_cycle[st.session_state.current_question % 3]

    # Show prompt and input
    user_answer = st.text_input(f"{elem[mode]} (enter the other two)")
    submit = st.button("Submit")

    if submit and user_answer:
        answer = user_answer.strip().split()
        correct = [str(elem['name']), str(elem['symbol']), str(elem['number'])]
        correct.remove(str(elem[mode]))

        if sorted(answer) == sorted(correct):
            st.write("Correct!")
            st.session_state.score += 1
        else:
            st.write(f"Wrong. Correct answer: {' '.join(correct)}")

        st.session_state.current_question += 1
        st.experimental_rerun()
else:
    # Quiz finished
    elapsed = time.time() - st.session_state.start_time
    st.write(f"Quiz finished! Your score: {st.session_state.score}/{len(st.session_state.elements)}")
    st.write(f"Time taken: {elapsed:.2f} seconds")
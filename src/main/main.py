# app.py
import random
import time
import streamlit as st

st.set_page_config(page_title="Periodic Table Quiz", layout="centered")

# --- Data ---
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
    {"name": "Zirconium", "symbol": "Zr", "number": 40},
]

# --- Helpers ---
def reset_quiz_state():
    keys = ["mode", "elements", "index", "score", "start_time", "running"]
    for k in keys:
        if k in st.session_state:
            del st.session_state[k]

def start_quiz(mode: str):
    st.session_state.mode = mode
    st.session_state.elements = ELEMENTS.copy()
    random.shuffle(st.session_state.elements)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.running = True

def format_correct(correct):
    return " ".join(map(str, correct))

def evaluate_answer(user_text: str, correct):
    # Compare tokenized answers ignoring case and order
    user_tokens = [t.strip().lower() for t in user_text.split() if t.strip()]
    correct_tokens = [str(t).strip().lower() for t in correct]
    return sorted(user_tokens) == sorted(correct_tokens)

# --- UI ---
st.title("Periodic Table Quiz")
st.write("Functional, keyboard-friendly quiz. Type `STOP` in the answer box to quit at any time.")

# Mode selection + start controls in the sidebar
with st.sidebar:
    st.header("Controls")
    chosen_mode = st.radio("Choose mode", options=["random", "number", "name", "symbol"])
    if not st.session_state.get("running", False):
        if st.button("Start Quiz"):
            start_quiz(chosen_mode)
    else:
        if st.button("Stop and Reset"):
            reset_quiz_state()

# If quiz not running -> show info
if not st.session_state.get("running", False):
    st.info("Select a mode and press **Start Quiz** in the sidebar.")
    st.write("Modes:")
    st.write("- **random**: cycles between prompts (number → name → symbol).")
    st.write("- **number / name / symbol**: the prompt will be that field; you must provide the other two fields.")
    st.write("Examples of acceptable answers: `O Oxygen 8`, `O 8` (order doesn't matter).")
    st.write(f"Number of elements available: {len(ELEMENTS)}")
    st.stop()

# Quiz is running
elements = st.session_state.elements
idx = st.session_state.index
elem = elements[idx]
mode = st.session_state.mode
total = len(elements)

# Determine prompt and correct answers
if mode == "random":
    qtype = idx % 3  # 0 -> show number, 1 -> show name, 2 -> show symbol
    if qtype == 0:
        prompt_text = f"Element with atomic number: {elem['number']}"
        correct = [elem["name"], elem["symbol"]]
    elif qtype == 1:
        prompt_text = f"Element with name: {elem['name']}"
        correct = [elem["symbol"], str(elem["number"])]
    else:
        prompt_text = f"Element with symbol: {elem['symbol']}"
        correct = [elem["name"], str(elem["number"])]
else:
    # non-random: prompt is the chosen mode, expect the other two
    prompt_text = f"Element with {mode}: {elem[mode]}"
    correct = [str(elem["name"]), str(elem["symbol"]), str(elem["number"])]
    # remove the shown value from correct answers
    correct.remove(str(elem[mode]))

# Display progress and timer
elapsed = time.time() - st.session_state.start_time
st.subheader(f"Question {idx + 1} / {total}")
st.write(f"Mode: **{mode}** • Elapsed: **{elapsed:.1f}s** • Score: **{st.session_state.score}**")

# Answer form
with st.form(key="answer_form"):
    user_input = st.text_input(label=prompt_text, placeholder="Type your answer (tokens separated by spaces)")
    submit = st.form_submit_button("Submit")

if submit:
    if user_input.strip().upper() == "STOP":
        st.warning("Quiz stopped by user. Resetting.")
        reset_quiz_state()
        st.experimental_rerun()

    if not user_input.strip():
        st.warning("Empty answer — please type something or STOP to quit.")
    else:
        if evaluate_answer(user_input, correct):
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong. Correct answer: {format_correct(correct)}")

        st.session_state.index += 1

        # finished?
        if st.session_state.index >= total:
            duration = time.time() - st.session_state.start_time
            st.balloons()
            st.write("---")
            st.subheader("Quiz finished")
            st.write(f"Final score: **{st.session_state.score} / {total}**")
            st.write(f"Total time: **{duration:.2f} seconds**")
            if st.button("Play again (same mode)"):
                # restart with same mode
                start_quiz(st.session_state.mode)
                st.experimental_rerun()
            if st.button("Play again (choose mode)"):
                reset_quiz_state()
                st.experimental_rerun()
            if st.button("Quit"):
                reset_quiz_state()
                st.experimental_rerun()
        else:
            # continue to next question (re-run will show next prompt)
            st.experimental_rerun()
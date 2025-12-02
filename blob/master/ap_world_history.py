#!/usr/bin/env python3
"""
Two-key AP World History practice quiz.
Prompt types: 'name' (give info) or 'info' (give name).
After each response the correct answer is shown and you decide whether to award credit.
Type STOP to quit at any time.
"""

import random
import time
import shlex

ITEMS = [
    {"name": "Qing Dynasty",
     "info": "Last imperial dynasty of China; founded in 1644 by the Manchus and ruled China for more than 260 years; expanded China's borders to include Taiwan, Tibet, Chinese Central Asia, and Mongolia; preceded by the Ming Dynasty and succeeded in 1912 by the Republic of China."},

    {"name": "Manchus",
     "info": "Northeast Asian peoples who defeated the Ming Dynasty and founded the Qing Dynasty in 1644; established the last of China's imperial dynasties."},

    {"name": "Mughal Empire",
     "info": "Muslim state (1526-1857) exercising dominion over most of India in the sixteenth and seventeenth centuries; often had difficulties managing a large, diverse empire; practiced Sunni Islam."},

    {"name": "Ottoman Empire",
     "info": "Islamic state of Turkic-speaking peoples lasting from roughly 1299 to 1922; conquered Byzantium (1453) and was based at Istanbul; encompassed lands in the Middle East, North Africa, the Caucasus, and eastern Europe; famed for gunpowder armies and Janissaries."},

    {"name": "Safavids",
     "info": "A Shi'ite Muslim dynasty that ruled in Persia (Iran and parts of Iraq) from the 16th–18th centuries; culture mixed Persian, Ottoman, and Arab influences."},

    {"name": "Songhai Empire",
     "info": "Islamic West African empire (15th–16th c.) that expanded as Mali declined; controlled trans-Saharan trade and centers of Islamic learning; effectively destroyed after Morocco's 1591 invasion."},

    {"name": "Devshirme",
     "info": "Ottoman system by which boys from Christian communities were taken to serve as Janissaries (elite military units), usually converted to Islam and trained for state service."},

    {"name": "Janissaries",
     "info": "Elite Ottoman infantry formed from the devshirme system; often converted to Islam and used gunpowder weapons such as muskets."},

    {"name": "Samurai",
     "info": "Class of salaried warriors in feudal Japan who served a daimyo in return for land or rice; pledged loyalty within a strict honor code."},

    {"name": "Divine Right",
     "info": "The doctrine that monarchs are God's representatives on earth and are therefore accountable only to God."},

    {"name": "Absolute Monarchy",
     "info": "A system of government in which the head of state is hereditary and the sovereign holds near-complete centralized power."},

    {"name": "Versailles",
     "info": "Palace constructed by Louis XIV outside Paris to glorify royal power and subdue the nobility; late 17th–early 18th century."},

    {"name": "Zamindars",
     "info": "Decentralized landholders/tax collectors in the Mughal system who collected tribute/taxes for the emperor."},

    {"name": "Taj Mahal",
     "info": "Mausoleum in India built by Mughal emperor Shah Jahan; completed in 1649 in memory of his favorite wife; blends Indian and Islamic architectural elements with Quranic calligraphy."},

    {"name": "Tax farming",
     "info": "A tax-collection system (used by the Ottomans and others) where private contractors collected taxes for a fee, often generating state revenue for expansion."},

    {"name": "Protestant Reformation",
     "info": "Religious movement begun by Martin Luther in 1517 that criticized Catholic practices and led to the formation of Protestant denominations (Lutheran, Calvinist, Anglican, etc.)."},

    {"name": "95 Theses",
     "info": "Arguments written by Martin Luther against certain Church practices; posted October 31, 1517; a catalyst for the Protestant Reformation."},

    {"name": "Martin Luther",
     "info": "German monk who challenged Catholic Church practices in 1517 with the 95 Theses and helped spark the Protestant Reformation."},

    {"name": "Counter/Catholic Reformation",
     "info": "Catholic Church's reaction to the Protestant Reformation: reaffirmed papal authority, reformed abuses (ended sale of indulgences), created Jesuit order, and prosecuted heresy via the Inquisition."},

    {"name": "Jesuits",
     "info": "A Catholic teaching and missionary order founded during the Counter-Reformation to defend Catholicism and engage in education and missions worldwide."},

    {"name": "Indulgence",
     "info": "A pardon sold by the Catholic Church in exchange for repentance (and often payment); heavily criticized during the Reformation."},

    {"name": "Simony",
     "info": "The buying and selling of church offices; a corrupt practice addressed by Catholic reforms."},

    {"name": "Inquisition",
     "info": "Roman Catholic tribunal for investigating and prosecuting heresy; used extensively in Spain and Spanish territories."},

    {"name": "Thirty Years War",
     "info": "A large-scale conflict (1618–1648) rooted in religious and political struggles in the Holy Roman Empire; ended with the Peace of Westphalia."},

    {"name": "John Calvin",
     "info": "French theologian (1509–1564) who developed Calvinism, emphasizing predestination and strict moral discipline."},

    {"name": "Sikhism",
     "info": "Monotheistic religion founded in northern India in the 16th century by Guru Nanak; combines elements of Hinduism and Islam."},

    {"name": "Shogunate",
     "info": "Japanese military government led by a shogun who held actual power while the emperor remained a figurehead."},

    {"name": "Daimyo",
     "info": "Feudal Japanese lords who commanded private samurai armies and owed allegiance to the shogun."},

    {"name": "Jizya",
     "info": "A tax levied on non-Muslims (Christians and Jews) in some Islamic states, permitting them religious autonomy."},

    {"name": "Millet System",
     "info": "Ottoman system dividing subjects into religious communities (millets) with autonomous self-government under their own leaders."},

    {"name": "Sakoku",
     "info": "Japan's isolationist policy under the Tokugawa shogunate (1603–1868) that severely limited foreign trade and contact."},
]

def normalize_text(s: str):
    """Simple normalization for token-based comparison."""
    # shlex.split handles quoted phrases reasonably; then lower-case and strip punctuation
    try:
        tokens = shlex.split(s)
    except ValueError:
        tokens = s.split()
    cleaned = []
    for t in tokens:
        t = t.strip().lower()
        # keep alphanumerics and common punctuation within words
        t = "".join(ch for ch in t if ch.isalnum() or ch in ("-", "_"))
        if t:
            cleaned.append(t)
    return sorted(cleaned)

def auto_match(user_text: str, correct_text: str) -> bool:
    """Return True if token sets are identical (helpful hint only)."""
    return normalize_text(user_text) == normalize_text(correct_text)

def start_quiz():
    print("AP World History — Two-key Practice Quiz")
    print("Type 'STOP' to quit at any time.\n")

    modes = ("random", "name", "info")
    while True:
        mode = input("Choose mode (random/name/info) [random]: ").strip().lower()
        if not mode:
            mode = "random"
        if mode in modes:
            break
        print("Invalid mode. Choose one of:", ", ".join(modes))

    items = ITEMS.copy()
    random.shuffle(items)
    score = 0
    attempted = 0
    start_time = time.time()

    for idx, item in enumerate(items, start=1):
        # pick prompt direction
        if mode == "random":
            ask_info = (idx % 2 == 0)  # alternate prompt type
        else:
            ask_info = (mode == "name")  # if mode == name, prompt name -> expect info

        if ask_info:
            prompt = f"Provide the INFO for: {item['name']}\n> "
            correct = item["info"]
            expected_label = "INFO"
        else:
            # show the info truncated first line for readability if very long
            preview = item["info"].split(".")[0]
            prompt = f"Provide the NAME for: {preview}...\n> "
            correct = item["name"]
            expected_label = "NAME"

        user_input = input(f"Q{idx}/{len(items)} | Elapsed: {time.time() - start_time:.1f}s\n{prompt}")
        if user_input.strip().upper() == "STOP":
            print("\nQuiz stopped by user.")
            break
        if not user_input.strip():
            print("Empty response recorded. You may award credit manually after seeing the correct answer.\n")

        # Show correct answer and an automatic-match hint, then ask user to award credit
        print("\nCorrect answer:")
        print(f"{expected_label}: {correct}\n")
        match = auto_match(user_input, correct)
        print(f"Auto-match suggestion: {'YES' if match else 'NO'} (token comparison)\n")

        # Ask user whether to award credit
        while True:
            award = input("Award credit for this response? (y/n) [n]: ").strip().lower()
            if award == "":
                award = "n"
            if award in ("y", "yes", "n", "no"):
                break
            print("Please answer 'y' or 'n' (or press Enter for no).")
        attempted += 1
        if award in ("y", "yes"):
            score += 1
            print("Credit awarded.\n")
        else:
            print("No credit awarded.\n")

    duration = time.time() - start_time
    print("Session summary")
    print("----------------")
    print(f"Questions attempted: {attempted}")
    print(f"Score (user-awarded): {score}")
    print(f"Total time: {duration:.2f} seconds")
    print("Thank you for practicing.")

if __name__ == "__main__":
    start_quiz()

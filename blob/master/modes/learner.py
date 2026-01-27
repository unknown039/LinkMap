import copy
import random
import sys
import time
from collections import Counter

from lcs2 import lcs_length

from blob.master.modes.editor import ReturnToBeginning

def learner_mode(copied_data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G",
     "H", "I", "J", "K", "L", "M",
     "N", "O", "P", "Q", "R", "S",
     "T", "U", "V", "W", "X", "Y", "Z"]

    while True:
        data = copy.deepcopy(copied_data)
        score = 0

        while True:
            subject = input("Subject: ").strip().lower()

            keyword_checker(subject)

            if subject not in data:
                print("Subject not found\n")
            else:
                break

        while True:
            quiz = input("Quiz: ").strip().lower()

            keyword_checker(quiz)

            if quiz not in data[subject]:
                print("Quiz not found\n")
            elif not data[subject][quiz]:
                print("Quiz is empty. Please choose another one\n")
            else:
                print()
                break

        quiz_length = len(data[subject][quiz])
        current_quiz = list(data[subject][quiz].values())
        random.shuffle(current_quiz)

        print(f"Number of questions: {quiz_length}")
        print()

        start_time = time.time()
        total_points = 0
        points_possible = 0

        for current_question_number in range(quiz_length):
            correct_answer = ""
            user_is_correct = None
            points_earned = None
            current_question = current_quiz[current_question_number]

            print(f"Q{current_question_number + 1}/{quiz_length} ({quiz}) | Score: {score} | Elapsed: {time.time()-start_time:.1f}s")

            if current_question[-1] == "MC":
                points_possible = 1
                correct_answer = current_question[1].strip().lower()

                print(f"Question: {current_question[0]}")
                current_question.pop(0)
                current_question.pop()
                random.shuffle(current_question)

                for i in range(len(current_quiz[current_question_number])):
                    print(f"{alphabet[i]}. {current_quiz[current_question_number][i]}")
                    if current_quiz[current_question_number][i] == correct_answer:
                        correct_answer = alphabet[i].lower()

                answer = input(f"\nAnswer: ").strip().lower()

                if correct_answer == answer:
                    user_is_correct = True
                    points_earned = 1
                else:
                    user_is_correct = False
                    points_earned = 0

                correct_answer = correct_answer.upper()
            elif current_question[-1] == "SDR":
                points_earned = 0
                num_of_correct_answers = current_question[-2]
                correct_answers_raw = current_question[1:num_of_correct_answers + 1]
                correct_answers_list = list()
                correct_answer = ""
                points_possible = num_of_correct_answers
                point_should_cap = False

                print(f"{current_question[0]}")
                answers_list = current_question[1:-3]
                random.shuffle(answers_list)

                for i in range(len(answers_list)):
                    print(f"{alphabet[i]}. {answers_list[i]}")

                    if answers_list[i] in correct_answers_raw:
                        correct_answers_list.append(alphabet[i].lower())
                        correct_answer += alphabet[i].upper() + ","

                answers = input(f"\nAnswer: ").strip().lower().split(",")
                user_is_correct = True

                for answer in answers:
                    if answer.lower() in correct_answers_list:
                        points_earned += 1
                    else:
                        user_is_correct = False
                        point_should_cap = True
                if len(answers) < len(correct_answers_list):
                    user_is_correct = False

                correct_answer = correct_answer[:-1].upper()
                if points_earned > point_should_cap and point_should_cap:
                    points_earned = current_question[-3]
            elif current_question[-1] == "M":
                points_earned = 0
                longest_string_length = 0
                shortest_string_length = sys.maxsize
                max_char_per_line = 60
                elements_list = current_question[:-2]
                prompt = current_question[-2]
                points_possible = len(elements_list)
                unpacked_list = list(set([element for sublist in elements_list for sub_sub_list in sublist for element in sub_sub_list]))
                random.shuffle(elements_list)
                random.shuffle(unpacked_list)
                correct_answer = "Placeholder for matching"

                for element in unpacked_list:
                    if len(element) > longest_string_length:
                        longest_string_length = len(element)
                    if len(element) < shortest_string_length:
                        shortest_string_length = len(element)

                for element in elements_list:
                    random.shuffle(element)

                all_elements_string = join_and_wrap_lines(unpacked_list, " | ", max_char_per_line)

                for i in range(len(elements_list)):
                    if elements_list[i][0] == ['']:
                        index_chosen = 1
                    else:
                        index_chosen = 0

                    print(f"\nElements:\n"
                          f"{all_elements_string}")

                    print(f"{prompt}")
                    user_answer = input(f"({','.join(elements_list[i][index_chosen])}): ").split(",")
                    print()

                    if (index_chosen == 1 or index_chosen == 0) and Counter(user_answer) == Counter(elements_list[i][index_chosen ^ 1]):
                        points_earned += 1
                        print(f"Correct!")
                    else:
                        user_is_correct = False
                        print(f"Incorrect")
            elif current_question[-1] == "S":
                correct_sequence = current_question[2:-1]
                shuffled_list = random.sample(correct_sequence, len(correct_sequence))
                # NOTE: this shuffle and copy the list
                prompt = current_question[0]
                partial_credit = current_question[1] == "Y"
                user_answers = list()

                for i in range(len(correct_sequence)):
                    if i == 0:
                        print(f"Elements:\n"
                              f"{join_and_wrap_lines(shuffled_list, " | ")}")
                    else:
                        print(f"-----------------------------------------------------\n\n"
                              f"Elements:\n"
                              f"{join_and_wrap_lines(shuffled_list, " | ")}")

                    print(f"{prompt}")
                    user_answers.append(input(f"{i + 1}. "))
                    print()

                if partial_credit:
                    points_earned = 0 if lcs_length(correct_sequence, user_answers) == 1 else lcs_length(correct_sequence, user_answers)
                    points_possible = len(correct_sequence)
                elif user_answers == correct_sequence:
                    points_earned = 1
                    points_possible = 1
                else:
                    points_earned = 0
                    points_possible = 1

                user_is_correct = points_earned == points_possible


            if user_is_correct:
                print(f"Correct!\n")
            else:
                if current_question[-1] == "MC" or current_question[-1] == "SDR":
                    print(f"Incorrect. The answer is {correct_answer}.\n")
                elif current_question[-1] == "M":
                    print(f"Correct answers: ")

                    for element in current_question[:-2]:
                        print(f"({', '.join(element[0])} ⇔ {', '.join(element[1])})")
                    print()

            score += points_earned
            total_points += points_possible

        print(f"Quiz Finished!")
        print(f"Final score: {score}/{total_points}")
        print(f"Total time: {time.time()-start_time:.1f}s\n")

        continue_quiz = input("Do you want to continue in learner mode? (Y/N): ").lower().strip()

        if continue_quiz == "y":
            continue
        else:
            return

def keyword_checker(response, score=-1):
    from .. main import end_learning

    response = response.lower().strip()

    if response == "back":
        raise ReturnToBeginning()
    elif response == "stop" and score != -1:
        end_learning()
        print("Score:", score)
    elif response == "stop" and score == -1:
        end_learning()

def join_and_wrap_lines(list_of_strings, delimiter, max_char_per_line=60):
    all_elements_string = ""
    temp_string_holder = ""
    longest_string_length = 0

    for string in list_of_strings:
        if len(string) > longest_string_length:
            longest_string_length = len(string)

    for i in range(len(list_of_strings)):
        if not list_of_strings[i]:
            continue
        elif len(temp_string_holder + list_of_strings[
            i]) % max_char_per_line + 3 >= max_char_per_line - longest_string_length \
                or i == len(list_of_strings) - 1:
            all_elements_string += temp_string_holder + list_of_strings[i] + "\n"
            temp_string_holder = ""
        else:
            temp_string_holder += list_of_strings[i] + delimiter

    return all_elements_string
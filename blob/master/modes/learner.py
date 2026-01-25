import copy
import random
import time

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

        for current_question_number in range(quiz_length):
            correct_answer = ""
            user_is_correct = None
            points_earned = None
            current_question = current_quiz[current_question_number]

            print(f"Q{current_question_number + 1}/{quiz_length} ({quiz}) | Score: {score} | Elapsed: {time.time()-start_time:.1f}s")

            if current_question[-1] == "MC":
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
            elif current_question[-1] == "SDR":
                points_earned = 0
                num_of_correct_answers = current_question[-2]
                correct_answers_raw = current_question[1:num_of_correct_answers]
                correct_answers_list = list()

                print(f"Question: {current_question[0]}")
                answers_list = current_question[1:-2]

                for i in range(len(answers_list)):
                    print(f"{alphabet[i]}. {answers_list[i]}")

                    if answers_list[i] in correct_answers_raw:
                        correct_answers_list.append(alphabet[i].lower())

                    answers = input(f"\nAnswer: ").strip().lower().split(",")
                    user_is_correct = True

                    for answer in answers:
                        if answer in correct_answers_list:
                            points_earned += 1
                        else:
                            user_is_correct = False
                            points_earned -= 1


            if user_is_correct:
                score += points_earned
                print(f"Correct!\n")
            else:
                print(f"Incorrect. The answer is {correct_answer.upper()}.\n")

        print(f"Quiz Finished!")
        print(f"Final score: {score}/{quiz_length}")
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

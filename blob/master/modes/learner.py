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
            answer = None
            correct_answer = None
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

            if answer == correct_answer:
                score += 1
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

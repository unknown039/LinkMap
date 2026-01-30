class ReturnToBeginning (Exception):
    pass

def editor_mode(data, end):
        while True:
            subject_level = input("Create subject or modify existing subject (C/M): ").lower().strip()

            if subject_level == "finished":
                return
            else:
                keywords_checker(subject_level)

            subject = None
            subject_is_chosen = False

            while not subject_is_chosen:
                subject = input("Subject: ").lower().strip()
                print()

                if subject == "finished":
                    if not data[subject]:
                        data[subject] = {}
                    end()
                elif subject_level == "m" and subject not in data:
                    print("That subject does not exist.")
                    continue
                else:
                    keywords_checker(subject)

                    if subject_level == "c" and subject not in data:
                        data[subject] = {}
                        subject_is_chosen = True
                    elif subject_level == "c" and data[subject]:
                        print("There is already a subject under this name.")

                        while True:
                            subject_choice = input(f"Choose a different name or modify this subject (C/M): ").lower().strip()

                            if subject_choice == "finished" or subject_choice == "back" or subject_choice == "stop":
                                print("Keywords are not allowed right now. Please pick (C/M)\n")
                            elif subject_choice == "m":
                                subject_is_chosen = True
                                break
                            elif subject_choice == "c":
                                data[subject] = {}
                                subject_is_chosen = True
                                break
                            else:
                                continue
                    elif subject_level == "m" and data[subject]:
                        subject_is_chosen = True
                        continue

            quiz_level = input("Create a quiz or modify existing quiz (C/M): ").lower().strip()

            if quiz_level == "finished":
                return
            else:
                keywords_checker(quiz_level)

            different_quiz_edit = False

            while not different_quiz_edit:
                quiz = input("Quiz Name: ").lower().strip()

                if quiz == "finished":
                    return
                else:
                    keywords_checker(quiz)
                    # TODO: Make sure all conditions are expected

                    if quiz_level == "c" and quiz in data[subject]:
                        print(f"\nThere is already a quiz under this name.")

                        while True:
                            quiz_choice = input(f"Choose a different name or modify this quiz (C/M): ").lower().strip()

                            if quiz_choice == "finished" or quiz_choice == "back" or quiz_choice == "stop":
                                print("Keywords are not allowed right now. Please pick (C/M)\n")
                            elif quiz_choice == "m":
                                different_quiz_edit = True
                                break
                            elif quiz_choice == "c":
                                data[subject][quiz] = {}
                                different_quiz_edit = True
                                break
                            else:
                                continue
                    elif quiz_level == "m" and not data[subject][quiz]:
                        print(f"\nThe quiz under this name is either empty or not initialized.")

                        while True:
                            quiz_choice = input("Do you want to edit another quiz or modify this quiz anyways? (E/M) ").lower().strip()

                            if quiz_choice == "finished" or quiz_choice == "back" or quiz_choice == "stop":
                                print("Keywords are not allowed right now. Please pick (C/M)\n")
                            elif quiz_choice == "e":
                                different_quiz_edit = True
                                break
                            elif quiz_choice == "m":
                                different_quiz_edit = False
                                break
                            else:
                                continue
                    elif quiz_level == "c" and quiz not in data[subject]:
                        data[subject][quiz] = {}

                if different_quiz_edit:
                    different_quiz_edit = False
                    continue
                else:
                    break


            print()

            last_type_of_assessment_item = None
            quiz_questions_dictionary = data[subject][quiz]
            current_question_number = len(data[subject][quiz])
            print(f"Number of questions in quiz: {current_question_number}")

            while True:
                current_question_number += 1
                if last_type_of_assessment_item is None:
                    last_type_of_assessment_item = input(f"Choose one type of assessment items to add:\n"
                                                                 f"(MC)  Multiple Choice\n"
                                                                 f"(SDR) Selected-Response\n"
                                                                 f"(M)   Matching\n"
                                                                 f"(S)   Sequence\n"
                                                                 f"(SC)  Set Completion\n"
                                                                 f"(SR)  Short Response\n").strip().lower()

                    if last_type_of_assessment_item == "finished":
                        return
                    else:
                        keywords_checker(last_type_of_assessment_item)
                else:
                    print()
                    adding_question_decision = input("Do you want to add another question? (Y/N) ").strip().lower()
                    if adding_question_decision == "n":
                        print()
                        data[subject][quiz] = quiz_questions_dictionary
                        break
                    elif adding_question_decision == 'finished':
                        print()
                        data[subject][quiz] = quiz_questions_dictionary
                        return
                    elif adding_question_decision == 'y':
                        pass
                    else:
                        keywords_checker(adding_question_decision)
                        print("Please enter Y, N, or one of the keywords")
                        current_question_number -= 1
                        continue



                    while True:
                        same_type = input("Do you want to continue adding the same type of assessment items? (Y/N) ").strip().lower()
                        if same_type == "n":
                            last_type_of_assessment_item = input(f"\nChoose one type of assessment items to add:\n"
                                                                 f"(MC)  Multiple Choice\n"
                                                                 f"(SDR) Selected-Response\n"
                                                                 f"(M)   Matching\n"
                                                                 f"(S)   Sequence\n"
                                                                 f"(SC)  Set Completion\n"
                                                                 f"(SR)  Short Response\n"
                                                                 ).strip().lower()
                            break
                        elif same_type == "y":
                            break
                        elif same_type == "finished":
                            print()
                            data[subject][quiz] = quiz_questions_dictionary
                            return
                        else:
                            keywords_checker(adding_question_decision)
                            print("Please enter Y, N, or one of the keywords")
                            current_question_number -= 1
                            continue

                print()

                if last_type_of_assessment_item == "mc":
                    question = input("Question: ")
                    quiz_questions_dictionary[current_question_number] = [question] + input("Answers: ").strip().split(",") + ["MC"]
                elif last_type_of_assessment_item == "sdr":
                    while True:
                        num_of_correct_answers = input("How many correct answers are there? ").strip().lower()
                        if num_of_correct_answers == "finished":
                            print()
                            data[subject][quiz] = quiz_questions_dictionary
                            return
                        else:
                            keywords_checker(num_of_correct_answers)

                            try:
                                num_of_correct_answers = int(num_of_correct_answers)
                                break
                            except ValueError:
                                print(f"Please enter a number")
                                continue

                    while True:
                        partial_score_cap = input("Score Cap with Error(s): ")

                        if partial_score_cap == "finished":
                            print()
                            data[subject][quiz] = quiz_questions_dictionary
                            return
                        else:
                            keywords_checker(partial_score_cap)

                            try:
                                partial_score_cap = int(partial_score_cap)
                                break
                            except ValueError:
                                print(f"Please enter a number")
                                continue

                    question = input("Question: ")
                    quiz_questions_dictionary[current_question_number] = ([question] + input("Answers: ").strip().split(",")
                                                                          + [partial_score_cap] + [num_of_correct_answers]
                                                                          + ["SDR"])
                elif last_type_of_assessment_item == "m":
                    quiz_questions_dictionary[current_question_number] = []

                    while True:
                        element_set = input(f"Sets: ").split("~")

                        if len(element_set) == 1:
                            quiz_questions_dictionary[current_question_number].append(element_set[0])
                            quiz_questions_dictionary[current_question_number] = (quiz_questions_dictionary[current_question_number] + ["M"])
                            break
                        elif len(element_set) == 2:
                            quiz_questions_dictionary[current_question_number].append([element_set[0].split(","), element_set[1].split(",")])
                        else:
                            print("Enter a valid token or in the correct format according to the documentation. Keywords do not work here")
                elif last_type_of_assessment_item == "s":
                    quiz_questions_dictionary[current_question_number] = []
                    element_number = 0
                    quiz_questions_dictionary[current_question_number].append(input("Prompt: "))

                    if want_partial_credit():
                        quiz_questions_dictionary[current_question_number].append("Y")
                    else:
                        quiz_questions_dictionary[current_question_number].append("N")

                    while True:
                        element_number += 1
                        element = input(f"Element {element_number}: ")

                        if not element:
                            quiz_questions_dictionary[current_question_number].append("S")
                            break
                        else:
                            quiz_questions_dictionary[current_question_number].append(element)
                elif last_type_of_assessment_item == "sc":
                    # TODO: Add prompts to every set
                    # TODO: Warn about Duplicates

                    quiz_questions_dictionary[current_question_number] = []
                    set_number = 0
                    quiz_questions_dictionary[current_question_number].append(input("Prompt: "))

                    if want_partial_credit():
                        quiz_questions_dictionary[current_question_number].append("Y")
                    else:
                        quiz_questions_dictionary[current_question_number].append("N")

                    while True:
                        set_number += 1
                        set_of_elements = input(f"Set {set_number}: ").split(",")

                        if set_of_elements == [""]:
                            quiz_questions_dictionary[current_question_number].append("SC")
                            break
                        else:
                            quiz_questions_dictionary[current_question_number].append(set_of_elements)
                elif last_type_of_assessment_item == "sr":
                    quiz_questions_dictionary[current_question_number] = [input(f"Question: "),
                                                                          input(f"Answer: "),
                                                                          input(f"Max Points: "),
                                                                          "SR"]

def keywords_checker(response):
    from .. main import end_learning

    response = str(response).strip().lower()

    if response == 'back':
        raise ReturnToBeginning
    elif response == 'stop':
        end_learning()

def want_partial_credit():
    while True:
        allow_partial_credit = input(f"Allow partial credit (Y/N): ").strip().lower()
        if allow_partial_credit == "y":
            return True
        elif allow_partial_credit == "n":
            return False
        else:
            print(f"Enter Y or N")
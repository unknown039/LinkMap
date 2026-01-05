class ReturnToBeginning (Exception):
    pass

def editor_mode(data, end):
        while True:
            subject_level = input("Create subject or modify existing subject (C/M): ").lower().strip()

            if subject_level == "finished":
                return
            else:
                keywords_checker(subject_level)

            print()

            subject = input("Subject: ").lower().strip()

            if subject == "finished":
                data[subject] = {}
                end()
            elif subject_level == "m" and subject not in data:
                print("That subject does not exist.")
            else:
                keywords_checker(subject)

                if subject_level == "c":
                    data[subject] = {}

            quiz = input("Quiz Name: ").lower().strip()

            if quiz == "finished":
                data[subject][quiz] = {}
                return
            else:
                keywords_checker(quiz)
                data[subject][quiz] = {}

            print()

            last_type_of_assessment_item = None
            quiz_questions_dictionary = {}
            current_question_number = len(data[subject][quiz])

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
                        print()
                        if same_type == "n":
                            last_type_of_assessment_item = input(f"Choose one type of assessment items to add:\n"
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

                    question = input("Question: ")
                    quiz_questions_dictionary[current_question_number] = [question] + input("Answers: ").strip().split(",") + [num_of_correct_answers] + ["SDR"]
                elif last_type_of_assessment_item == "m":
                    quiz_questions_dictionary[current_question_number] = []

                    while True:
                        element_set = input(f"Sets: ").split()

                        if element_set[0].lower() == "matched":
                            quiz_questions_dictionary[current_question_number] = quiz_questions_dictionary[current_question_number] + ["M"]
                            break
                        elif len(element_set) == 2:
                            quiz_questions_dictionary[current_question_number].append([element_set[0].split(","), element_set[1].split(",")])
                        else:
                            print("Enter a valid token or in the correct format according to the documentation. Keywords do not work here")
                elif last_type_of_assessment_item == "s":
                    quiz_questions_dictionary[current_question_number] = []
                    element_number = 0

                    while True:
                        element_number += 1
                        element = input(f"Element {element_number}: ")

                        if not element:
                            quiz_questions_dictionary[current_question_number].append("S")
                            break
                        else:
                            quiz_questions_dictionary[current_question_number].append(element)
                elif last_type_of_assessment_item == "sc":
                    quiz_questions_dictionary[current_question_number] = []
                    set_number = 0

                    while True:
                        set_number += 1
                        set_of_elements = input(f"Set {set_number}: ").split(",")

                        if set_of_elements == [""]:
                            quiz_questions_dictionary[current_question_number].append("SC")
                            break
                        else:
                            quiz_questions_dictionary[current_question_number].append(set_of_elements)
                elif last_type_of_assessment_item == "sr":
                    quiz_questions_dictionary[current_question_number] = [input(f"Question: "), input(f"Answer: "), "SR"]

def keywords_checker(response):
    from .. main import end

    response = str(response).strip().lower()

    if response == 'back':
        raise ReturnToBeginning
    elif response == 'stop':
        end()
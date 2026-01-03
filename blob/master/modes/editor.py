class ReturnToBeginning (Exception):
    pass

def editor_mode(data, end):
    while True:
        subject_level = input("Create subject or modify existing subject (C/M): ").lower().strip()

        if subject_level == "finished":
            return
        else:
            keywords_checker(subject_level, end)

        print()

        subject = input("Subject: ").lower().strip()

        if subject == "finished":
            data[subject] = {}
            end()
        elif subject_level == "m" and subject not in data:
            print("That subject does not exist.")
        else:
            keywords_checker(subject, end)

            if subject_level == "c":
                data[subject] = {}

        quiz = input("Quiz Name: ").lower().strip()

        if quiz == "finished":
            data[subject][quiz] = {}
            return
        else:
            keywords_checker(quiz, end)
            data[subject][quiz] = {}

        finished_adding_questions = False
        last_type_of_assessment_item = None
        quiz_questions_dictionary = {}
        current_number_of_questions = 0

        while not finished_adding_questions:
            current_number_of_questions += 1
            if last_type_of_assessment_item is None:
                last_type_of_assessment_item = input(f"Choose one type of assessment items to add:\n"
                                                     f"(MC)  Multiple Choice\n"
                                                     f"(SDR) Selected-Response\n"
                                                     f"(M)   Matching\n"
                                                     f"(SR)  Short Response\n"
                                                     f"(S)   Sequence\n").strip().lower()

                if last_type_of_assessment_item == "finished":
                    return
                else:
                    keywords_checker(last_type_of_assessment_item, end)
            else:
                if input("Do you want to add another question? (Y/N) ").strip().lower() == "n":
                    print()
                    data[subject][quiz] = quiz_questions_dictionary
                    continue

                if input("Do you want to continue adding the same type of assessment items? (Y/N)").strip().lower() == "n":
                    last_type_of_assessment_item = input(f"Choose one type of assessment items to add:\n"
                                                         f"(MC)  Multiple Choice\n"
                                                         f"(SDR) Selected-Response\n"
                                                         f"(M)   Matching\n"
                                                         f"(SR)  Short Response\n"
                                                         f"(S)   Sequence\n").strip().lower()


            if last_type_of_assessment_item == "mc":
                question = input("Question: ")
                quiz_questions_dictionary[str(current_number_of_questions)] = [question] + input("Answers: ").strip().split(",") + ["MC"]
            elif last_type_of_assessment_item == "sdr":
                num_of_correct_answers = input("How many correct answers are there? ")
                question = input("Question: ")
                quiz_questions_dictionary[str(current_number_of_questions)] = [question] + input("Answers: ").strip().split(",") + [num_of_correct_answers] + ["SDR"]

def keywords_checker(response, end_function):
    from .. main import end

    response = str(response)

    if response == 'back':
        raise ReturnToBeginning
    elif response == 'stop':
        end_function()
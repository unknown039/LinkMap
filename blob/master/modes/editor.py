def editor_mode(data, end):
    print("Type FINISHED at any moment to save your changes. "
          "\nSTOP would end the program and discard your changes."
          "\nBACK would take you back to the beginning page (a.k.a the one that asks what would you like to do) and "
          "discard your changes.\n")
    subject_level = input("Would you like to add a new subject or proceed to an existing subject? (A/P) ").lower().strip()
    subject = input("Subject: ").lower().strip()

    if subject_level == "finished":
        return
    elif subject_level == "back":
        return
    elif subject_level == "stop":
        end()
    elif subject_level == "p" and data[subject] is None:
        print("That subject does not exist.")

    if subject == "finished":
        data[subject] = {}
        end()
    elif subject == "stop":
        end()
    elif subject == "back":
        return
    elif subject_level == "a":
        data[subject] = {}

    quiz = input("What quiz would you like to add? ").lower().strip()

    if quiz == "stop":
        end()
    elif quiz == "back":
        return
    elif quiz == "finished":
        data[subject][quiz] = {}
        return
    else:
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
        else:
            if input("Do you want to add another question? (Y/N) ").strip().lower() == "n":
                data[subject][quiz] = quiz_questions_dictionary
                end()

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
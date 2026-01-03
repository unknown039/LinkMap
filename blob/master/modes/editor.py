def editor_mode(data, end):
    print("Type FINISHED at any moment to save your changes. "
          "\nSTOP would end the program and discard your changes."
          "\nBACK would take you back to the beginning page (a.k.a the one that asks what would you like to do) and "
          "discard your changes.\n")
    subject_level = input("Would you like to add a new subject or proceed to an existing subject? (A/P) ").lower().strip()
    subject = input("Subject: ").lower().strip()

    if subject_level == "a":
        data[subject] = {}
    elif subject_level == "finished":
        return
    elif subject_level == "back":
        return
    elif subject_level == "stop":
        end()
    elif subject_level == "p" and data[subject] is None:
        print("That subject does not exist.")

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

    while not finished_adding_questions:

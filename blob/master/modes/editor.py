from dataclasses import dataclass, field
from typing import Literal, Optional

from blob.master.exception_classes import ReturnToBeginning


# Defaults allows incremental construction
@dataclass
class Question:
    type: Optional[str] = None
    prompt: Optional[str] = None
    points_worth: Optional[int] = None
    partial_credit: bool = False

@dataclass
class MultipleChoice(Question):
    type: Literal["MC"] = field(init=False, default="MC")
    correct_answer: Optional[str] = None
    answers_list: list[str] = field(default_factory=list)


@dataclass
class ShortResponse(Question):
    type: Literal["SR"] = field(init=False, default="SR")
    correct_answer: Optional[str] = None

def get_valid_number(prompt, number_type, lower_range, upper_range):
    while True:
        response = input(prompt)

        try:
            if number_type == "int":
                value = int(response)
            elif number_type == "float":
                value = float(response)
            else:
                print(f"{number_type} is not a supported type")
                continue

            if value < lower_range or value > upper_range:
                print(f"Must within {lower_range}-{upper_range}\n")
                continue

            return value
        except ValueError:
            print(f"{response} is not a number\n")

def get_boolean(prompt, true, false):
    true = true.lower()
    false = false.lower()

    while True:
        response = input(prompt).strip().lower()

        if response == true:
            return True
        elif response == false:
            return False

        print(f'{response} is not "{true}" or "{false}"\n')

def mc():
    question = MultipleChoice()
    question.prompt = input("Prompt: ")
    question.correct_answer = input("Correct Answer: ")
    question.answers_list.append(question.correct_answer)

    while True:
        incorrect_answer = input("Incorrect Answer: ")

        if not incorrect_answer:
            print()
            break

        question.answers_list.append(incorrect_answer)

    question.points_worth = get_valid_number("Points worth: ", "int", 1, float('inf'))
    print()

    return question

def sr():
    question = ShortResponse()
    question.prompt = input("Prompt: ")
    question.correct_answer = input("Correct Answer: ")
    question.points_worth = get_valid_number("Points worth: ", "int", 1, float('inf'))
    question.partial_credit = get_boolean("Allow partial credit: ", "Y", "N")
    print()

    return question

class Editor:
    def __init__(self, data, save):
        self.data = data
        self.save = save
        self.current_subject_name = None
        self.current_quiz_name = None
        self.quiz_questions_dictionary = None

    def editor_mode(self):
        while True:
            self.current_subject_name = self.get_subject()
            self.current_quiz_name = self.get_quiz()
            self.quiz_questions_dictionary = self.data[self.current_subject_name][self.current_quiz_name]
            quiz_length = len(self.quiz_questions_dictionary)

            print(f"There are currently {quiz_length} quiz questions.")

            while True:
                question_changes = self.check_and_prompt("Enter a number or abbreviation to add or modify a question: ")

                if question_changes.isdigit():
                    if question_changes not in self.quiz_questions_dictionary:
                        print("Question number not found\n")
                        continue
                    self.quiz_questions_dictionary[question_changes] = self.create_question()
                else:
                    self.quiz_questions_dictionary[str(quiz_length + 1)] = self.create_question(question_changes)

    def create_question(self, question_type=None):
        if question_type is None:
            question_type = self.check_and_prompt("\nQuestion Type: ")

        match question_type:
            case "MC":
                print(f"Keywords are now disabled\n")
                return mc()
            case "SR":
                print(f"Keywords are now disabled\n")
                return sr()
            case _:
                print(f"Invalid question type")
                return self.create_question()

    def get_subject(self):
        subject = self.check_and_prompt(f"Subject: ").lower()

        if subject in self.data:
            print(f"Modifying existing subject")
        else:
            print(f"Adding new subject")
            self.data[subject] = {}

        print()
        return subject

    def get_quiz(self):
        quiz = self.check_and_prompt("Quiz: ").lower()

        if quiz in self.data[self.current_subject_name] and self.data[self.current_subject_name]:
            print(f"Modifying existing quiz")
        else:
            print(f"Adding new quiz")
            self.data[self.current_subject_name][quiz] = {}

        print()
        return quiz

    def check_and_prompt(self, prompt):
        response = input(prompt).strip().upper()

        if response == 'SAVE':
            if self.current_subject_name and self.current_quiz_name and self.quiz_questions_dictionary:
                self.data[self.current_subject_name][self.current_quiz_name] = self.quiz_questions_dictionary

            self.save()
        elif response == 'BACK':
            print()
            raise ReturnToBeginning()
        elif response == 'STOP':
            raise SystemExit("Exiting LinkMap")

        return response
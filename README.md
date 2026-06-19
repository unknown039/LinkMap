# LinkMap
- A quiz-creating and learning application created using Python  
- Currently, there are only **2 types of assessment types**   
- There are 2 modes:
  - Editor
  - Learner  

*Except questions and answers, inputs are generally* **not case-sensitive**

After seeing the prompt:
> Editor/Learner:

Type "E" to go into editor mode, "L" to go into learner mode

---
## Editor Mode

### Subject
- Enter the name of the subject you want to modify or add
- If the program already have the subject within the data, the response 
will interpret as modifying the existing subject
- Else, the program will add a new subject

### Quiz
The rules are the same with subject

#### Example:
> Subject: Math  
> Modifying existing subject
> 
> Quiz: Algebra  
> Modifying existing quiz

---

### Adding Questions
- The program will print how many questions are in the quiz.
- If it prints there are 0 questions, that means there are no questions 
within the quiz
- Then, the program will prompt for a number of an abbreviation of a
question type

#### Example 1
> There are currently 3 quiz questions.  
> Enter a number or abbreviation to add or modify a question:

If an abbreviation is entered, the quiz will add a new question of the 
question type

#### Example 2
> There are currently 3 quiz questions.  
> Enter a number or abbreviation to add or modify a question: MC

- If a number is entered, it must be an integer ranging from 0 to the amount
of questions contained in the quiz. This will modify the question with
the same question number
- Then, the quiz will prompt for the abbreviation of the question type

#### Example 3
> There are currently 3 quiz questions.  
> Enter a number or abbreviation to add or modify a question: 1  
> 
> Question Type: MC

- Keywords are disabled once an abbreviation is accepted
- Repeat this process before using one of the keywords

### Multiple Choice
Abbreviation: **MC**  
1. Enter the prompt (a.k.a. question)
2. Enter the correct answer
3. Enter the incorrect answers
4. Repeat step 3 until you have all the incorrect answers entered
5. Enter nothing and press enter to finish entering incorrect answers
6. Enter how many points the question should be worth

### Example
> Prompt: What is 3 + 3?  
> Correct Answer: 6  
> Incorrect Answer: 5  
> Incorrect Answer: 4  
> Incorrect Answer: 3  
> Incorrect Answer: 
> 
> Points worth: 5

---

### Short Response
Abbreviation: **SR**

1. Enter the prompt (a.k.a. question)
2. Enter the correct answer
3. Enter how many points it is worth
4. Enter "Y" or "N" in enable or disable partial credit, respectively

### Example
> Prompt: What is multiplication?  
> Correct Answer: Repeated addition  
> Points worth: 5  
> Allow partial credit: Y
# LinkMap
- A quiz-creating and learning application created using Python  
- Currently, there are only **2 types of assessment types**   
- There are 2 modes:
  - Editor
  - Learner  

*Except questions and answers, inputs are generally* **not case-sensitive**

After seeing the prompt:
> Editor/Learner:

Input "E" to go into editor mode, "L" to go into learner mode  

*Note: Remember to hit enter*

---
## Keywords
Keywords are special strings that helps to control the program. There are 
currently 3 keywords:

- **STOP:** Immediately end the programs and discard any changes made
within the editor
- **BACK:** Go back to the beginning prompt, "Editor/Learner: "
- **SAVE:** Save any changes made within editor into the data storage. If
this keyword is not used before the program has ended, changes will be
discarded  

These keywords can generally be used everything except the following places:
- When adding a question in editor mode
- During a quiz in learner mode

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

---

## Learner Mode  

The mode will start with loading **two** machine learning model, which will
take some time to complete.

### Subject & Quiz

1. Enter the subject name (*must already exist within saved data*) 
2. Same for the quiz name
3. Type "T" to get feedback on every question or "F" to not get feedback. 
Feedback include whether the answer is correct and the correct answer if 
the learner's answer is incorrect.

### Example 1:
> Loading Sentence Transformer model: all-MiniLM-L6-v2  
> Loading Natural Language Inference model: DeBERTa-v3-base-mnli-fever-anli  
> This may take 10-30 seconds.  
>   
> Subject: math  
> Quiz: algebra  
> Instant Feedback: T

With instant feedback:
> 1\. What is multiplication?  
> Answer: Test incorrect answer  
> Incorrect: Repeated addition  
> 
>
> 2\. What is a number?  
> Answer: An object to represent quantity  
> Correct!

Without instant feedback:
> 1\. What is multiplication?  
> Answer: Test incorrect answer  
> 
> 
> 2\. What is a number?  
> Answer: An object to represent quantity

At the end, the quiz to print the amount of points (up to 2 decimal 
places) earned out of the possible amount of points and the percentage 
score (up to 2 decimal places). The decimal places usually comes up when
partial points are allowed on questions:

### Example 1:
> Score: 0/6 | 0.00%  

### Example 2: 
> Score: 0.76/6 | 12.73%  

Then, the process repeats and the learner is prompted for the subject

---

## Grading

### Multiple Choice

- Partial Credit Allowed: **No**
- Grading Method: **String Comparison**  
  - String match between learner and correct answer
  - Will NOT accept whole word answer
  - Only use the capital letters that are listed

**Correct Answer:**
> 1\. What is 1 + 2?  
> A. 2  
> B. 5  
> C. 3  
> D. 4
> 
> Answer: C

**Incorrect Answer:**
> 1\. What is 1 + 2?  
> A. 2  
> B. 5  
> C. 3  
> D. 4
> 
> Answer: 3

---

### Short Response

- Partial Credit Allowed: **Yes**
- Grading Method WITHOUT partial credit: **String Comparison**  
  - String match between learner and correct answer
  - Case-sensitive
- Grading Method WITH partial credit: NLI & Cosine Similarity 
  1. Use NLI gate to only let logically similar sentences to earn points 
  2. Use cosine similarity score to determine semantic similarity 
  3. Multiply semantic similarity score by the total amount of points the
  question worth

#### NLI Model (deberta)
Evaluate the relationship between the learner and correct answer  

**Entailment:** the probability if statement A is true, statement B is
also true

> The animal is NOT moving.  
> The dog is walking.

This combination will produce a high contradiction score

> The animal is moving.  
> Math is fun.

This combination will produce a high neutrality score

> The animal is moving.  
> The dog is walking.

This combination will produce a high entailment score

If the **entailment score is less than 0.5, neutrality score is greater 
than 0.75, OR contradictionary score is greater than 0.75,** the learner
will receive **0 credit** for the answer.  

### Sentence Embedding Model (all-MiniLM-L6-v2)

- As demonstrated, entailment score still is not very precise in scoring (
e.g. animal ↔ dog still produce somewhat high scores)
- A sentence embedding model (also known as sentence transformer) is used 
to determine how semantically similar the learner and correct answer are
- Its drawback is that it misevaluate logical similarity (e.g. not true 
↔ true have high similarity)
- The NLI model is used in conjunction to cover this weakness

Cosine similarity score returns how semantically similar two sentences
are between 0-1, ranging from unrelated to exact string match

### Limitations of Grading Method
While the models do provide somewhat accurate feedback on short response,
there are still major limitations. Here is a list of them:

- Numerical Reasoning
  - "The population is 100,000" vs "The population is 1,000,000"
  - "25% of 200 is 40" vs "25% of 200 is 50"
  - "The interest rate is 10%" vs "The interest rate is 100%"
- Comparison Reasoning
  - "The pie cost at least $10" vs "The pie cost more than \$10"
  - "There are exactly 5 pencils" vs "There are about 5 pencils"
  - "It takes more than 10 minutes" vs "It takes about 10 minutes"
- Units
  - 60 seconds vs 1 minute
  - 1 km vs 1000 m
  - 1 inch vs 2.54 cm
- Any specialized knowledge the models are not trained on
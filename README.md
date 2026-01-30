# LinkMap

---

LinkMap is a personal project that aims to emulate many different types of 
educational measurements using only text that are allowed within the terminal.  

It allows users to customize their quizzes and evaluate them according to 
their needs and study their own quizzes.  

Currently, LinkMap have **two** modes and a system:  

1. **Editor Mode**
2. **Learner Mode**
3. **Scoring System**  

Start by typing choosing the desirable mode. 

*The Scoring System section will include explanations on exactly what is each
assessment type*   
*Access to the **Scoring System** is currently unsupported*

---

## 1. Editor Mode

### LinkMap Keywords in Editor Mode:
- **FINISHED** at any moment to save your changes. 
- **STOP** would end the program and discard your changes.
- **BACK** would take you back to the beginning page (a.k.a. the one that asks
what would you like to do) and discard your changes.  
  
These keywords function everywhere in Editor Mode except when the program 
prompts for questions and answers.  

*They do not work in learner mode*

### Structure
 
Follow the instructions and answer the questions provided by the prompts. If 
there is a conflict (e.g. modifying a subject that does not exist), the 
program will prompt for a different response.  

After a valid pair of subject and quiz are selected, choose an assessment
type to add to the quiz.  

#### USE THE CAPITAL LETTERS IN THE LEFT WHEN CHOOSING THE TYPE

### LinkMap currently supports 6 assessment item types:
- Multiple Choice
- Selected-Response
- Matching
- Sequence
- Set completion
- Short Response

---

### Multiple Choice  

- Enter the question 
- Enter the list of answers
  - ***The first answer in the list will be chosen as the correct answer.***

**Example:**  
>Question: Which of the following is prime?  
>Answers: 2,6,4,9

In the example above, "2" will be chosen as the correct answer.

---

### Selected-Response

- Enter the amount of correct answers (zero is a valid option)
- Set your Score Cap with errors
  - If the learner choose an incorrect answer, their score cannot go above 
  the score cap
  - Enter nothing if a score cap is unwanted - NOT recommended as the user 
  can pick all answers to always gain full credit
- Enter the question
- Enter the answers separated by a comma
  - Using the amount of correct answers, the program will mark the first 
  answers as correct. 

**Example 1:**  

> How many answers are there? 3  
> Score Cap with Error(s): 2  
> Question: Which of the following are prime?  
> Answers: 2,3,5,9  

In the example above, the correct answers will be 2,3, and 5. If the 
learner pick number 9, regardless of their other options, they cannot gain 
more than 2 points.
  
**Example 2:**

> How many answers are there? 2  
> Score Cap with Error(s):   
> Question: Which of the following are prime?  
> Answers: 2,5,1,9  

In the example above, the correct answers will be 2 and 5. If the learner
pick any wrong answers, there score will be not be capped, so they have the
option to pick every answer to guarantee full credit.

---

### Matching

- Enter two sets separated by a "~"
- Within each set, each element is separated by a comma
- To finish, enter nothing

*Empty sets are accepted*

**IMPORTANT:**   
Each "sets" prompt is for a SINGLE match. The program will only assume that
the two sets match with each other and nothing else.

**Example 1:**
> Sets: Story,Literature~Math,Algebra  
> Sets: Art,Painting~Science   
> Sets: History,culture~  
> Sets:

In the example above, the set (Story, Literature) will be matched with the set
(Math, Algebra); (Art,Painting) will be matched with (Science); and (History,
culture) will be matched with nothing.   

*See scoring system for more information*

---

### Sequence

- Enter the prompt
- Decide if partial credits are allowed
- Enter the elements in sequence
- Enter nothing to finish

**Example 1:**

> Prompt: Sort the numbers from least to greatest  
> Allow partial credit (Y/N): Y  
> Element 1: 1  
> Element 2: 2  
> Element 3: 3  
> Element 4:

In the example above, the correct answer will be saved as (1, 2, 3).

---

### Set Completion

- Enter a prompt
- Decide if partial credit is allowed
- Enter each set with elements separated by a comma
- Enter nothing to finish

**Example:**

> Prompt: Each set have a symbol, atomic number, and element name  
> Allow partial credit (Y/N): Y  
> Set 1: H,1,Hydrogen  
> Set 2: He,2,Helium  
> Set 3: Li,3,Lithium  
> Set 4: 

In the example above, 3 sets are stored: (H, 1, Hydrogen), (He, 2, Helium),
(Li, 3, Lithium).

---

### Short Response

- Enter the question
- Enter the answer
- Enter the max amount of points (how many points the question is worth)

**Example:**

> Question: Explain the difference between a natural number and an integer.  
> Answer: A natural number is all positive whole numbers starting from 1. 
> An integer is all whole numbers that can be negative, positive, or zero.

---

# Learner Mode

Start by choosing an exiting subject and quiz pair. Then, the learner can 
answer the questions that are selected from the quiz in a specific format.  

The format the learner should abide for each assessment type is provided
below.  

---

### Multiple Choice  

After reading the prompt and considering the options, the learner should 
pick the correct **CAPITAL LETTER** that corresponds with the answer.

**Example:** 
> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> Which of the following are primes?  
> A. 2  
> B. 9  
> C. 8  
> D. 4
>  
> Answer: A  
> Correct!  

---

### Selected-Response  

After reading the prompt and considering the options, the learner should 
pick the correct **CAPITAL LETTERS** that corresponds with the answer,
separated by a comma.

**Example:** 
> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> Which of the following are primes?  
> A. 2  
> B. 9  
> C. 8  
> D. 5  
> E. 6
>  
> Answer: A,D  
> Correct!  

---

### Matching

The learner is provided with a list of elements. Then, the learner is 
provided by a set of elements, and they choose all the elements from the list
that matches with the provided set separated by a comma.

**Example 1:**  

> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> Lithium | He | Helium | Li | 1 | 2 | 3 | Hydrogen | H  
>   
> (Hydrogen): H,1  
>   
> Correct!  

It is possible for a set to be matched with nothing.  

**Example 2:**

> Lithium | He | Helium | Li | 1 | 2 | 3 | Hydrogen | H | Iron  
>   
> (Iron): 
>   
> Correct!  

---

### Sequence

The learner is provided with a list of all the elements to be sorted into 
sequence one at a time.  

**Example:**

> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> Elements:  
> 1 | 5 | 2 | 4 | 3  
> 
> Test sequence prompt    
> 1\. 1  
> 
> \-----------------------------------------------------
> 
> Elements:  
> 1 | 5 | 2 | 4 | 3  
> 
> Test sequence prompt  
> 2\. 2  
> 
> \-----------------------------------------------------
> 
> Elements:  
> 1 | 5 | 2 | 4 | 3  
> 
> Test sequence prompt  
> 3\. 3 
> 
> \-----------------------------------------------------
> 
> Elements:
> 1 | 5 | 2 | 4 | 3  
> 
> Test sequence prompt  
> 4\. 4
> 
> \-----------------------------------------------------
> 
> Elements:  
> 1 | 5 | 2 | 4 | 3
> 
> Test sequence prompt  
> 5\. 5
> 
> Correct! 

---  

### Set Completion

The learner is provided with one member of the set, then the user provide
all the other elements.  

**Example:**

> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> Each set contains the atomic number, atomic symbol, and element name  
> 
> Hydrogen: H,1  
> He: Helium,2  
> 3: Li,Lithium  

---  

### Short Response  

The learner is provided with a prompt. Then, they answer it.  

**Example:**

> Q1/1 (test quiz) | Score: 0 | Elapsed: 0.0s  
> I wonder if I just put something really terrible here. Will literally 
> anybody notice?  
> Yeah, I think they will notice.  

---


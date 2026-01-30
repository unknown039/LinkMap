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

## Scoring System  

The default system (which, as of 2026-01-29, is uncustomizable) is based on
the Educational Measurement & Assessment Theory field. This involves the 
systematic process of evaluating, quantifying, and improving student 
learning, skills, and educational outcomes.

However, this project DOES NOT closely integrate all the nuances of each tasks as the future will simply
allow more customization for the scoring. So, the explanation of the task
within the field is provided alongside with LinkMap emulation to provide the
similarities and differences.

The answers and score is updated immediately after the learner enters their
answer.  

---  

### Multiple Choice

#### Task Explanation

- **Setup:** The examinee is provided with a prompt and a list of answers,
typically labeled with alphabet letters


- **Goal:** Their goal is to choose ONE answer from the list that
answers the question.   


- **Points:** This task is usually worth 1 point. 

#### LinkMap Task Scoring

After randomizing the list of answers, the correct answer is mapped upon the
correct letter. If the user pick the correct letter, that would correspond to
picking the correct answer, and the learner will earn a point.  

---

### Selected-Response  

#### Task Explanation

- **Setup:** The examinee is provided with a prompt and a list of answers,
typically labeled with alphabet letters  
  

- **Goal:** Their goal is to choose ALL answers from the list that answers
the question. Typically, at least one answer must be selected, but this is
not always the case.  


- **Points:** There are typically 3 different type of scoring. 
  - All or Nothing Scoring: If the examinee do not select ALL the correct 
  answers, they gain no credit.
  - Penalty Scoring: The examinee gain a point for every correct answer 
  selected and lose a point for every incorrect answer selected.
  - Partial Credit with a Function: There are many different ways this could
  be implemented. Typically, the examinee gain a point for each selected 
  answer. Then, their score is capped if they selected an incorrect answer.
  
#### LinkMap Task Scoring

LinkMap currently supports All or Nothing Scoring and a common type of 
Partial credit with a Function. The LinkMap function for partial credit
allows the user to set a fixed score cap on the question if the learner
select an incorrect answer.

---

### Matching 

#### Task Explanation

- **Setup:** The examinee is provided with 2 columns. The premise (question)
column on the left and the response (answer) column on the right
  

- **Goal:** The examinee match each element on the left column with one or 
more element on the right column. Typically, all elements on the left is 
matched with at least one element on the right, but there can be exceptions.
Elements on the right column can have elements that is not a match for any
element on the left column, usually called "Distractors".


- **Points:** Per-pair scoring is the most common and reliable method of
scoring. This system gives the examinee a point for every match they 
correctly identified. This does allow the examinee to simply brute-force
identifying all possible matches, but the amount of matches grows incredibly
quickly with the size of the columns, so it is not a problem unless the 
sample is very small.

#### LinkMap Task Scoring

LinkMap supports per-pair scoring, but it has many caveats.  

First, the  formatting is not perfectly correct. Instead of providing the 
learner two separated lists of elements, LinkMap give them a random 
assortment of all the elements within the list. 

Second, the answering format is that each element from the list is randomly
picked to be the premise, so the program sometimes will pick the "answer"
as the premise. However, this is not a problem since the system will still 
allow the editor to capture all possible relationships between the 
elements, but it is much more difficult to create this assessment type.  

---

### Sequence

#### Task Explanation

- **Setup:** The examinee is provided with a list of randomized elements and
typically some prompt
  

- **Goal:** The examinee then sorts the list into a sequence with some sort
of rule or ordering.


- **Points:** All-or-Nothing is a simple metric to use for scoring in 
sequence, but it is very harsh on the examinee. A more common and modern
metric used is the LCS, or Longest Common Subsequence.
  - Longest Common Subsequence: LCS of two sequences is the longest sequence
  of elements that appears in both sequences in the same relative order (not
  necessarily contiguously)—LCS scoring awards credit proportional to the 
  length of that subsequence between the correct sequence and the student’s 
  response. 
  - *This definition is AI-generated*

#### LinkMap Task Scoring

LinkMap supports both type of scoring and have the identical setup described
above.

---

### Set Completion

#### Task Explanation

- **Setup:** The examinee is given a list of unordered sets to memorize. On
the examination, they are given a randomly selected member of the set for
every set.
  

- **Goal:** They have to produce all the other members of the set.


- **Points:** The examinee gain a point per member they correctly recalled
within a set.

#### LinkMap Task Scoring

LinkMap scoring and setup is identical to what is described above.


---

### Short Response

#### Task Explanation

- **Setup:** The examinee is provided with a prompt.
  

- **Goal:** They answer the prompt through writing (a.k.a. typing)


- **Points:** Criteria for points varies greatly in many different subjects.
Typically, the semantically closer their answer is to the sample answer,
the higher their points.

#### LinkMap Task Scoring

LinkMap setup is identical to what is described above. It uses a sentence
transformer (a.k.a. a text AI) to compare how semantically close the 
learner's answer is to the provided answer. The amount points given to the
learner is proportional to the maximum amount of points and the 
embedding similarity.
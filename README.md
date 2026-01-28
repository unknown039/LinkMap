# Editor Mode

### LinkMap Keywords in Editor Mode:
- **FINISHED** at any moment to save your changes. 
- **STOP** would end the program and discard your changes.
- **BACK** would take you back to the beginning page (a.k.a. the one that asks what
would you like to do) and discard your changes.  
  
These keywords work everywhere except the prompt for questions and answers.

### LinkMap currently supports 6 assessment item types:
- Multiple Choice
- Selected-Response
- Matching
- Sequence
- Set completion
- Short Response

### Multiple Choice
The user is provided with a question and a list of answers.
User select ONE answer as the correct answer.

In editor mode, separate the answers using commas with the first one being correct.

Example:  
"answer1,answer2,answer3,answer4,answer5" - answer1 is the correct answer

### Selected-Response

the user is provided with a question a list of answers. User select multiple 
answers as correct answers in the same format as entering them in the editor.

In editor mode, the program will ask how many correct answers there are, n (zero is a 
valid option). Next, set your Score Cap with errors. This means that if the learner 
select an incorrect answer, then **their score cannot go above the Score Cap. Enter nothing
if there is no score cap (not recommended).  

Then, the program will prompt for the answers. It will pick
the first n answers as the correct one. If you use the keyword "FINISHED" during this 
time, the program will discard information about the number of correct answers.

Example:  
"How many answers are there? 3"  
"answer1,answer2,answer3,answer4,answer5" - answer1, answer2, and answer3 are the correct answers


### Matching

The user is provided with a set of elements, and they must provide all elements in the 
other set, separated by a ~.  

Example (Program Provided "(Boy, Girl): "):  
(Boy,Girl): (Male,Female)  

In Editor Mode, the user must provide their sets in this format:    

Set: element1~elementA  
Set: element2~elementB  
Set: element3~elementC

The two sets are in parentheses and are separated by spaces (there can be as many 
spaces as needed, but there must be at least one)  

When finished, type a string for the prompt of the question without using a ~.  
Empty sets and single element sets are accepted.

### Sequence
The user is provided with a set of elements that must rearranged in the correct order. To 
complete the task, they will enter the elements in the same format in the editor. 

In Editor Mode, enter the elements one at a time in the correct order. To finish, enter 
nothing.

Example:  

Prompt: You can leave this empty     
Allow Partial Credit (Y/N): Y   
Element 1: This  
Element 2: is   
Element 3: an   
Element 4: example  
Element 5:   

Saved sequence: ("this", "is", "an", "example")  

### Set Completion
The user is provided with an element of a set, and they provide all other elements of the
set.  

**IMPORTANT:** If the user enters more elements than needed to complete 
the set, the extra elements will be ignored when scoring.  
Partial credit 

Example:

Prompt goes here

1: Hydrogen,H  
He: Helium,2
Lithium: 3,6.94,Li

In the example above, the Hydrogen and Helium sets are correct. The 
Lithium set is either incorrect or have partial credit because the "Li" 
is ignored IF 6.94 was not part of the answer and the set only had 3 members

In Editor Mode, separates the element in the set by a comma. Enter nothing to finish. The
amount of elements within each set can vary

Example:

Prompt: This could be blank
Allow partial credit (Y/N): Y
Set 1: Hydrogen,1  
Set 2: Helium,2,He,4.0026  
Set 3: Lithium,3,Li  
Set 4:  

Stored set of sets: [(Hydrogen,1), (Helium,2,He,4.0026), (Lithium,3,Li)]  

### Short Response
The user is provided with a question, and they must provide the answer  

In Editor Mode, simply enter the question, hit enter, then enter the answer, and hit 
enter. It is highly recommended to enter a number as the max score for partial credit, 
but you could also enter nothing, and the program will default to scoring as one.


# Learner Mode

### LinkMap Keywords in Editor Mode:
- **STOP** would end the program immediately and show your score (if there is one).
- **BACK** would take you back to the beginning page (a.k.a. the one that asks what
would you like to do).  


- [ ] TODO: Fix up the README.md file
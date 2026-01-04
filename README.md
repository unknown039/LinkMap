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
answers as correct answers  

In editor mode, the program will ask how many correct answers there are, n (zero is a 
valid option), followed by prompting the options for the answers. The program will pick
the first n answers as the correct one. If you use the keyword "FINISHED" during this 
time, the program will discard information about the number of correct answers.

Example:  
"How many answers are there? 3"  
"answer1,answer2,answer3,answer4,answer5" - answer1, answer2, and answer3 are the correct answers


### Matching

The user is provided with a set of elements, and they must provide all elements in the 
other set, separated by a /.  

Example (Program Provided (Boy, Girl)):  
(Boy, Girl): (Male, Female)  

In Editor Mode, the user must provide their sets in this format:  
element1,element2,element3,... elementA,elementB,elementC,...   

The two sets are in parentheses and are separated by spaces (there can be as many spaces as needed, but there must be at least one)  

When they are finished, they should type "MATCHED". This will take them back to the first page in Editor Mode.  
Empty sets and single element sets are accepted.
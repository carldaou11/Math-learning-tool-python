# Math-learning-tool-python
Simple math quiz. The user is asked to answer randomly addition, subtraction, or multiplication

	SPRCIFICATIONS:
Write a python program, a quiz math tool that helps students to practice on basic math operation (addition, subtraction, and multiplication). The program will return the score obtained.
 
Here is an example of a sample run, where the user entered 4 questions to be answered.
In this example the student or the quiz participant made 4 questions in total, and got a total score of 3 over 4. On average the participant answered 75% of the questions in 24s. The participant was timed to accomplish the math quiz from the moment the number of questions desired till the end of it. After each question, the program tells the user the number of correct answers (like a current score).
We got the average answered questions with the following formula:
(Total Score*100)/Number of total questions) = Average answered
Referring to the basic formula above, use the participant’s total score earned (3) multiplied by (100) then divided by the total number of question of the math quiz.






	Design
To do this program, I designed 6 functions. The first one is the math_learning_quiz. This is the main function of my program.
Pseudocode:
Enter how many question do you want to solve
Start the timer
For each question 
       Print the current question
       Verify the answer of the user by calling the function input answer
       If correct
           Update the current score
           Output correct answer
        Else
           Output incorrect
Call the function design so the participant know he is done
Output the total score
Output the average 
Output the time taken
The function output the average using the formula presented upward, and the time taken to do the quiz.
The 2 design function are here to give some design to the program at the beginning of the run and at the end.
The function input answer check the answer entered by the user.

The function generate question is a math related question. It will generate randomly the question of the math quiz tool.
PseudoCode:
Implementation of the generate_question
Create a list of operators +, -, *
Generate number1 from 1 to 20
Generate number2 from 1 to 20
Randomly select 1 operator from the list
If the operand is +
    Answer = num1+num2
Elif operand is –
    Answer = num1-num2
Elif operans is * 
     Answer = num1*num2
Output the question

The function checks input check whether the input entered by the participants is valid or not the user cannot enter an alphabetical letter or a number with decimal. The function takes as argument the input entered by the user.
Pseudocode:
Implementation of the check input function
Create a variable checker
Create a list of digits from 0 to 9
For each digit of the input
   If index of checker is not in the list of digits
     Return false
Return true

A sample run of the code to see the method in action:
 
	Implementation
Check the python file.

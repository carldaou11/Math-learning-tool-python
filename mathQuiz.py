#Author Carl Daou
#id 2017023568

import random
import time


# function for math learning quiz, it is the main function of the code
def math_learning_quiz():
    design()
    x = input("Enter how many questions you want: \n")
    while(checkInput(x) == False):
        x = input("Invalid input, enter numbers only:\n")
    x = int(x)
    print("You will be timed to solve " + str(x) + "questions.")
    # score at the begining of the quiz is 0
    score = 0
    # start the timer
    start_time = time.time()
    # for loop N times (depends on the user)
    for i in range(x):
        print("\nQuestion Number:", i + 1)
        # call function
        correct = input_answer()

        # if correct score increase
        if correct:
            score = score + 1
            print('Correct!')
            print("Your score is :", score)
        else:
            print('Incorrect Answer!')
            print("Your score is :", score)

    # Here are the results obtained at the end
    design1()
    print("Your total score is : ", score, "over", x)
    print("On Average Percentage :", (score * 100) / x)

    print("######Congrats! It took you %s  seconds to solve the quiz ######" % (time.time() - start_time))


def checkInput(input):
    checker = str(input)
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(0,len(checker)):
        if checker[i] not in numbers:
            return False
    return True

# this function is a design fuction just as a title or a welcome to the quiz
def design():
    intro = "### Carl Daou Math Quiz ###"
    print("#" * len(intro))
    print(intro)
    print("#" * len(intro))


def design1():
    conclusion = "### Thank you for solving my quiz. I recommend you to pracice a lot and become good in calculus.  ###"
    print("#" * len(conclusion))
    print(conclusion)
    print("#" * len(conclusion))


# function to check the answer entered by the user
def input_answer():
    # first of all a question should be generated
    answer = generate_question()
    # the answer can now be entred by the user
    User_Answer = input()
    while(checkInput(User_Answer)==False):
       User_Answer = input("Invalid input, enter numbers only:\n")
    User_Answer = int(User_Answer)
    # return if both user answer entered on the keyboard and the answer computed by the program are equal
    return User_Answer == answer


# This function will generate the questions of the quiz and their answer
def generate_question():
    # list of operator, list of operations available for my quiz
    operators = ['+', '-', '*']
    # generate two number randamly using the random module
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # randamly select 1 operator from list, so the questions displayed are shuffled
    opera = random.choice(operators)
    # calculate the answer according to the operator randomly selected from the list of operators
    if opera == '+':
        answer = num1 + num2
    elif opera == '-':
        answer = num1 - num2
    elif opera == '*':
        answer = num1 * num2
    # print question
    print("What is", num1, opera, num2, " ? ")
    # return  the answer of the question
    return answer


# For sure we can add more operators to the quiz
# Call my main function
math_learning_quiz()

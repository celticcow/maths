#!/usr/bin/python3

import random

def ask_multiply():
    num1 = int(random.randint(0, 10))
    num2 = int(random.randint(0, 10))

    print("please Multiply : ", end="")
    print(str(num1) + " * " + str(num2) + " = ")

    answer = num1 * num2

    user_answer = int(input())

    if(user_answer == answer):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(answer))
        return(0)
#end of ask_multipy

def ask_divide():
    num1 = int(random.randint(1, 10))
    num2 = int(random.randint(1, 10))

    product = num1 * num2

    print("please Divide : ", end="")
    print(str(product) + " / " + str(num1))

    user_answer = int(input())

    if(user_answer == num2):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(num2))
        return(0)
#end ask_divide

def main():
    print("welcome to maths")

    """
    some of these will become toggle as we test more
    and advance
    """
    mode = "multiply"

    grade = 0
    for i in range(10):
        print(i)
        #grade += ask_multiply()
        #grade += ask_divide()

    print("you got " + str(grade) + " out of 10")

    
#end of main

if __name__ == "__main__":
    main()
#end of program
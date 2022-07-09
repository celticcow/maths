#!/usr/bin/python3

import random

def ask_multiply(upper = 10):
    num1 = int(random.randint(0, upper))
    num2 = int(random.randint(0, upper))

    print("please Multiply : ", end="")
    print(str(num1) + " * " + str(num2) + " = ")

    answer = num1 * num2

    while(True):
        try:
            user_answer = int(input())
            break
        except (ValueError, TypeError):
            print("invalid input pls type a number")
            pass

    if(user_answer == answer):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(answer))
        return(0)
#end of ask_multipy

def ask_divide(upper = 10):
    num1 = int(random.randint(1, upper))
    num2 = int(random.randint(1, upper))

    product = num1 * num2

    print("please Divide : ", end="")
    print(str(product) + " / " + str(num1))

    while(True):
        try:
            user_answer = int(input())
            break
        except (ValueError, TypeError):
            print("invalid input pls type a number")
            pass

    if(user_answer == num2):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(num2))
        return(0)
#end ask_divide

def ask_add(upper = 10):
    num1 = int(random.randint(0, upper))
    num2 = int(random.randint(0, upper))

    sum = num1 + num2

    print("please ADD : ", end="")
    print(str(num1) + " + " + str(num2) + " = ")

    while(True):
        try:
            user_answer = int(input())
            break
        except (ValueError, TypeError):
            print("invalid input pls type a number")
            pass
        
    if(user_answer == sum):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(sum))
        return(0)
    
#end of ask_add

def ask_subtract(upper = 10):
    num1 = int(random.randint(0, upper))
    num2 = int(random.randint(0, upper))

    if(num1 < num2):
        num1, num2 = num2, num1
    diff = num1 - num2

    print("pls SUBTRACT : ", end="")
    print(str(num1) + " - " + str(num2) + " = ")

    while(True):
        try:
            user_answer = int(input())
            break
        except (ValueError, TypeError):
            print("invalid input pls type a number")
            pass

    if(user_answer == diff):
        print("CORRECT")
        return(1)
    else:
        print("sorry, the correct answer is : " + str(diff))
        return(0)
#end of ask_subtract

def main():
    print("welcome to maths")

    """
    some of these will become toggle as we test more
    and advance
    """
    #mode = "russell"
    mode = "phillip"

    grade0 = 0
    for i in range(10):
        if(mode == "russell"):
            grade0 += ask_multiply()
        else:
            grade0 += ask_add(5)

    grade1 = 0
    for i in range(10):
        if(mode == "russell"):
            grade1 += ask_divide()
        else:
            grade1 += ask_subtract(5)

    print("you got " + str(grade0) + " out of 10")
    print("you got " + str(grade1) + " out of 10")

    
#end of main

if __name__ == "__main__":
    main()
#end of program
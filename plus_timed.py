#!/usr/bin/python3

import time
import random

def ask_plus_question(test_num):
    debug = 1

    print(test_num)
    second = int(random.randint(0, 12))

    placement = int(random.randint(1, 2))

    if(placement == 1):
        print(str(second) + " + " + str(test_num) + " = ", end="")
    else:
        print(str(test_num) + " + " + str(second) + " = ", end="")

    answer = test_num + second

    user_ans = int(input())

    if(answer == user_ans):
        print("correct")
        return(1)
    else:
        print("incorrect")
        return(0)

#end of ask_plus_question

def main():
    print("time for plus")

    target_number = 4
    time_start = int(time.time())

    score = 0

    for i in range(10):
        score = score + ask_plus_question(target_number)

    time_end = int(time.time())

    time_elapsed = time_end - time_start
    print(str(score) + " out of 5")
    print("in " + str(time_elapsed) + " seconds")

#end of main

if __name__ == "__main__":
    main()
#end
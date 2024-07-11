# multiplication table , it checks if the result is correct or not.

import numpy as np
import random

print("hello and welcome to the multiplication table check program")

first = random.randint(1,9)
second = random.randint(1,9)

int_result = first * second

print (first, "x" ,second, "= ?")

count = 0
max_try = 3

while count < max_try :
    guess = int(input("enter your guess: "))

    if guess == int_result :
        print("Correct!")
        break
    else:
        print("Incorrect!, try again")
        count += 1


if count == max_try :
    print("Used all your attempts,the correct answer is: ", int_result)

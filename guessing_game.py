#here is a game that guessing words

import random

print("Hello and welcome to the guessing game. ")
name = input ("What is your name?")
print("Good Luck" , name , "\n you have 7 attempts")

word_list = ["github", "desktop" , "medium" , "stack" , "overflow"]     #list

random_word = random.choice(word_list)                  #choses random one from the list

guess_length = len(random_word) * ["_"]                 #how many - 

attempts = 7

while attempts > 0:

    print("Guess the word:" + " ".join(guess_length))       #join adds between what is in it ""
    given_input = input("Enter a letter:" ).lower()

    if given_input in random_word:
        for index, letter in enumerate(random_word):         #enumerate for index matching letters
            if letter == given_input:
                guess_length[index] = given_input
        print("Correct word!" + " ".join(guess_length))
        
    else:
        attempts -= 1
        print(f"Incorrect letter! \n You have {attempts} attempts.")
        
        if "_" not in guess_length:
            print(f"congrats! ,your word is '{random_word}'")
            break
else:
    print(f"You lost!,try again. The word was '{random_word}'")
        





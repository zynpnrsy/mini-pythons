#number guessing with binary search

print("Welcome to the number guessing game. \n Pick a number between 1 and 50.")
def binary_search():
    low = 1
    high = 60
    attempts = 0
    
    input("Press enter to continue. ")
    

    while low <= high:
        
        mid = (low + high) // 2
        attempts += 1
        print("Is this the number you thought?", mid)
        
        answer = input("For 'Yes' > Y \nIf it is not correct then, \nIs it higher or lower? \nFor Higher > H | For Lower > L ").lower()
        
    
        if answer == "y":
            print("The job is done")
            break
        elif answer == "l" :
            high= mid + 1 
        elif answer == "h" :
            low = mid - 1 
            
        else:
            print("Please enter H, L, or Y.")
        
        
        if low > high:
            print("Hmm, something went wrong. Did you change your number?")

            


binary_search()
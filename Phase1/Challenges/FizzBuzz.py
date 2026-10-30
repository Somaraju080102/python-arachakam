#Number guessing game
#Computer picks a random number 1-100 (import random). The user has 7 tries and gets “higher/lower” hints. Handle non-numeric input without crashing (use isdigit() for now, proper exceptions come in Topic 8). Use while with break and the loop else for the “you lost” message.

import random 

random_number = random.randint(1, 100)
tries = 7


while tries > 0:
    inputVal=int(input("Guess a number between 1 and 100: "))
    print(f"your Number is {inputVal} and the random number is {random_number}")
    if(inputVal<random_number):
        print("Lower Bro")
        tries-=1;
    elif(inputVal>random_number):
        print("Higher Bro")
        tries-=1;
    elif(inputVal==random_number):
        print("You guessed it right")
        break
else:
    print("You lost!")
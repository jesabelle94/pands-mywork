# Messing with while loops
# Author: Jenny Formentera

# Modify the program in 3 (guess2.py) above, so that the program tells the user if there guess is too high or too low, each time they guess. HINT: put an if statement inside the while loop

import random # generate random number must type 'import > random'

# reference: https://www.linkedin.com/pulse/building-number-guessing-game-python-can-arslan/

Number = random.randint(0,100)
guess = int(input("Please guess the number: "))

while guess != Number: 
    # MAKE SURE TO ADD SPACE HERE TO STOP LOOP
    if guess < Number:
        print("Too low!")
        guess = int(input("Please guess again: "))
    # MAKE SURE TO ADD SPACE HERE TO STOP LOOP
    else:
        print("Too high!")
        guess = int(input("Please guess again: "))
    # MAKE SURE TO ADD SPACE HERE TO STOP LOOP
print("Well done! Yes the number was", Number) # adding the comma + the Number formula to guess will stop it.


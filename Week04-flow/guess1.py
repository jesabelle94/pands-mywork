# Messing with while loops
# Author: Jenny Formentera

# Write a program (guess1.py) that prompts the user to guess a number, 
# the program should keep prompting the user to guess the number until the user gets the right on

Number = 30

guess = int(input("Please guess the number:")) # this prompts the user to guess
while guess != Number: 
    print ("Wrong") # will print wrong if guesses wrong
    guess = int(input("Please guess again:")) # will prompt to ask again if entered a wrong number

print("Well done! Yes the number was", Number) # adding the comma + the Number formula to guess will stop it.


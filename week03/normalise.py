# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one
# Please enter a string: Some StRiNg
# That String normalised is :some string
# we reduced the input string from 57 to 11 characters

#Author: Jenny Formentera

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That String Normalised is : {normalisedString}")
print(f"we reduce the input string from {lengthOfRawString} to {lengthOfNormalised} characters")
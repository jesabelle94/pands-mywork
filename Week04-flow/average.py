# This number reads in numbers until
# the user enters 0
# it will tell then print back out again
# and their average

numbers = [0] # list of numbers

number = int(input("Enter number (0 to quit):"))

while number != 0:
    numbers.append(number) # appends adds a single item to certain collection types

    number = int(input("enter another (0 to quit): ")) # stops after you enter 0

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print(f"averahe is {average}")
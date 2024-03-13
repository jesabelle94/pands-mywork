# Messing with lists
# The code examples are in the jupyter notebook in course mater
# Author: Andrew Beatty

'''
boats = ['Sigma', 23, [1,2,3], {} ] # the square brackets [] is an empty list and add any variable type in it

len (boats) # this will list how many list you have in the list

print(len (boats)) 
'''

'''
boats = ['Sigma', 23, [1,2,3], {} ]

for boat in boats: # this will list each type of boat in the boats list
    print(type(boat))

'''

ages = [12,21,23,34] # list of ints 

sum = 0 
for age in ages:
    sum += age # this will calculate the sum of all ages / this will not calculate strings
print(sum)
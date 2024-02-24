# Messing with for loops

# for elem in list:
    # do something

# for number in range(1,10)
    # do something

boats = ['Signma', 'x yacht', 'Swan'] # create a list for example boats = to name of boats

for boat in boats:
    print("i'd rather be out in a ", boat, sep="") # the ', sep=="' separates / ',end=' puts them in one one / '\n\n"' puts a line break in each of them

for i in range(1,10): # this will count up to 10 not including 10
    print(i)

print ("all done i is now", i)

if "Swan" in boats: # make sure the word is exactly from the list, if it was 'swan' it will not print it
    print("that is a boat")
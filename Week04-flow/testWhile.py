# Messing with while loops

count = 0       # how to count from 0 to 9
while (count < 10): # this will count up to 9 as its less than 10
    print("count is ", count) # the comma prints each number from the count
    count = count + 1 # add this part to stop the inifinite loop or ctrl c without this part

print ("at the end count is ", count) # prints the end of the count which is 10

count = 10      # how to program a countdown backwards
while count >=0: # this will count up to 0 
    print("countdown ", count)
    count -= 1

print("blast off")

# sentinal controlled loop 

val = input("type something (q to quit):")
while val != 'q': # this will keep going until you input 'q'
    print ("hi mom")
    val = input("q to quit:") # once 'q' is inputted it will quit and print all done

print("all done")
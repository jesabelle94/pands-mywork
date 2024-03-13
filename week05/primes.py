# Generate primes
# Author: Andrew Beatty

primes = [] 
upto = 100000

for candidate in range(2, upto): # this should count up from 2 up to 100
    # print (candidate)
    isPrime = True # assuming it is a prime
    for divisor in primes: #  only need to check if divisable by prime
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break #jump out of the for loop

    if isPrime:
        primes.append(candidate) # this will add the prime numbers in the empty list (row 4)

print (primes)
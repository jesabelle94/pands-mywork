# Messing with dictionary
# Author: Andrew Beatty

car = {
    "make" : "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags" : ["pre-owned", "Best Buy", "Dealer"]

}

#print (car)

#for key in car: # how to print the different types of keys within the dictionary
#    print (key, ' has value' , car[key])

for key, value in car.items():
    print(key, 'has a value ', value)
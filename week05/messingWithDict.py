# Messing with dictionaries
# Author: Andrew Beatty
# You can have dictionary inside a dictionary (as many as you like)

car = { # car is of type of Dictionary
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner" : {
        "name" : "andrew",
        "driver-number" : 1123
    }
}

print (car["year"]) # this print specific info eg. year
print(car["owner"]) # this prints the owner objects
print(type(car["owner"].get("names"))) # type and .get are easier way to get info from the list if it exist
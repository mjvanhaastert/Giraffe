import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!

from math import sqrt
print(sqrt(25))


#we starten met het aanmaken van een functie die een valua number bij zich heeft
def cube(number):
    #nadat de functie is aangeroepen en een value heeft gekregen returnen we hem terug nadat we deze berekening hebben uitgevoerd
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False



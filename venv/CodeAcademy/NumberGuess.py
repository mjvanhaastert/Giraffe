"""
Rol een dobbelsteen en gok de uitkomst.
"""
#import een verschillende librairies
from random import randint
from time import sleep

#start van de functie
def get_user_guess():
    #we vragen hier om input van de gebruiker en die slaan we dan op in de variable guess.
    #we willen een rond cijfer hebben dus een int is hier de perfecte oplossing
    guess = int(input("Guess a number: "))
    #we willen dit natuurlijk terug geven
    return guess

def roll_dice(number_of_sides):
    #omdat dit werkt met 2 dobbelstenen en het totaal van die 2 nemen we 2 variables
    #we willen natuurlijk dat er automatisch een random cijfer te voorschijn komt dus
    #randint lost dat op voor ons. omdat we wel steeds verschillende cijfers willen hebben
    #koppelen we de 2de waarde aan number_of_sides. zo kunnen we zelf, nadat we de functie opvragen
    #steeds een andere cijfer invoeren
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    #omdat we natuurlijk wel een regel aan de gebruiker willen stellen en omdat we 2 dezelfde dobbelstenen
    #willen lossen we dit op door de number_of_sides gewoon simpel maal 2 te doen.
    max_val = number_of_sides * 2
    #hier laten we de max cijfer even zien aan de gebruiker
    print("The maximum possible value is: %d" % max_val)
    #we koppelen hier de input van de gebruiker aan de variable guess(ook al hebben we die al een keer genoemd
    #, we gebruiker hebben gewoon opnieuw omdat het duidelijke taal is dat kan namelijk in python) we moeten
    #namelijk de input hier kunnen gebruiken
    guess = get_user_guess()
    #nu moeten we natuurlijk een gebeurtenis creeeren.
    if guess > max_val:
        print("No guessing higher then the maximum possible value!")
    else:
        print("Rolling...")
        sleep(2)
        print("First roll %d" % first_roll)
        sleep(2)
        print("Second roll %d" % second_roll)
        sleep(2)
        total_roll = first_roll + second_roll
        print(total_roll)
        print("Result...")
        sleep(1)
        if guess == total_roll:
            print('You won!')
        else:
            print('You lost... ooh well try again')

roll_dice(6)
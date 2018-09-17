"""""
Deze calculator helpt de gebruiker om vormen te berekenen
door te vragen welke vorm de gebruiker wil uitrekenen. Neemt
de afmetingen op en print het dan uit om aan de gebruiker te laten zien.

"""
#Geeft een melding op het scherm dat het programma klaar is voor gebruik
print('1 moment ik ben even aan het opstarten... oke ik ben klaar voor gebruik')

#om te weten welke vorm de gebruker wil uitrekenen hebben we iets nodig
#dit doen we met een inputveld hiermee stellen we gewoon een vraag aan de
#gebruiker en kunnen we input in een variable zetten
name = input("Enter C for Circle or T for Triangle: ")
#nu zetten we de input in een variable zodat we hem later kunnen gebruiken
option = name
#We doen een check hier welke letter ingevoerd is bij input en als de invoer
#de letter C or c is dan word deze if statment uitgevoerd
if option == "C" or option == "c":
    print("Je hebt de option voor Circle ingevoerd")
    #om iets te berekenen moeten we de radius weten dus vragen we de gebruiker
    #om die in tevoeren zodat we die kunnen opslaan in de variable radius
    radius = float(input("Voer de radius in: "))
    #nu moeten we natuurlijk de omtrek uitrekenen en opslaan in een new variable
    area = 3.14159*(radius**2)
    #nu printen we het antwoord uit
    print("De omtrek van de Circle is %s" % area)
    #Anders word deze if statement uitgevoerd
elif option == "T" or option == "t":
    #een melding die laat zien dat de gebruiker laat zien dat hij voor een
    #driehoek heeft gekozen.
    print("Je hebt voor de option voor Driehoek gekozen")
    #hier vragen we om de lengte van de driehoek en stoppen die in de variable
    #base zodat we die laten kunnen gebruiken
    base =float(input("Ik heb de lengte nodig hiervoor"))
    #we hebben ook de hoogte nodig dus laten we die ook in een variable zetten
    height = float(input("oh en ook de hoogte, bedankt"))
    #nu gaan we de 2 variable berekenen en het antwoord in deze variable zetten
    area = 0.5 *base * height
    print("De inhoud van een driehoek is: %s" % area)
else:
    #door else kan nu alle andere input blokken en een melding laten geven
    print("Sorry maar je kan alleen C of T invoeren")
print("oke dat was hard werk, tijd om mezelf af te sluiten")
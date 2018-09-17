#we moeten achter het woord dat ingevoerd worden "ay" zetten
#dus maken een string met de ay
pyg = "ay"

#we hebben een input veld nodig waar je een woord kan invoeren
original = input("Enter a word")

#een if statement om te checken of het woord wat ingevoerd word niet leeg is
#en een and check om alleen alphabetische letter te kunnen invoeren

if len(original) >0 and original.isalpha():
    #pak uit ingevoerd de input en zet het in de variable word maar zet alle
    #letter om naar kleine letters
    word = original.lower()
    #pak uit de variable word de eerste letter en zet die in deze variable
    first_letter = word[0]
    #deze nieuwe variable neemt de variable word en voegt daar aan toe de variable
    #first letter en de variable pyg. hier word nog niet de eerste letter van
    #de variable word weggehaald dus dat moeten we hierna nog doen
    new_word = word + first_letter + pyg
    #hierboven hebben we onze nieuwe woord klaarstaan maar we moeten alleen nog
    #even de eerste letter er afhalen, dat word gedaan met slice, we geven aan dat
    #we onze variable word willen starten vanaf de 2de letter tot met het eind
    new_word = new_word[1:len(new_word)]
    #als de checks kloppend zijn dan mag je uitvoeren
    print(new_word)



else:
    #als de bovenste regels niet kloppende zijn dan wordt deze melding gegeven
    print("Sorry probeer het opnieuw")


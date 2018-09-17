wachtwoord = "sha256://salt:0a0///a0a0a"

#hier is hij in een array
print("Hier zitten ze in een array: " + str(wachtwoord.replace('/', '', 2).split(':')))
#hier hebben de 3 delen een eigen variable
sha256, salt, random = wachtwoord.replace('/', '', 2).split(':')
print("Eerste gedeelte in een eigen variable: " + sha256)
print("tweede gedeelte in een eigen variable: " + salt)
print("derde gedeelte in een eigen variable: " + random)

wachtwoord1 = "sha256://salt:0a0///a0a0a"

p, s, e = wachtwoord1.split(':')
print("Opties 3: " + p, s)




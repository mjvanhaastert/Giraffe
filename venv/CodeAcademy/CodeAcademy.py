(print ('Welcome to the Pig Latin Translator!')

# Start coding here!
 #input die vraagt om gegevens
original = raw_input("Enter a word:")
#if statement die kijkt naar de lengte van de aantal characters
#in dit geval of er minder dan nul zijn.
#dan hebben we nog een 2de check die controleerd of het alleen letters zijn
#en geen cijfers
if len(original) > 0 and original.isalpha():
  #Als de if en and checks correct zijn print dan mijn input uit
  print (original)
  #anders print het woord empty uit
else:
  print ("empty")


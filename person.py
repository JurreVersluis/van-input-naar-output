clearConsole = lambda: print('\n' * 150)

naam = input("Wat is uw naam?\n")
clearConsole()

adres = input("Wat is uw adres?\n")
clearConsole()

postcode = input("Wat is uw postcode?\n")
clearConsole()

woonplaats = input("Wat is uw woonplaats?\n")
clearConsole()

print("--------------------------------\n" + "--------------------")
print("|  Naam      :   " + str(naam))
print("|  Adres      :   " + str(adres))
print("|  Postcode      :   " + str(postcode))
print("|  Woonplaats      :   " + str(woonplaats))
print("--------------------------------\n" + "--------------------")
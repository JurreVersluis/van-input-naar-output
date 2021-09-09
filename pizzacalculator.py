# Jurre Versluis Pizza calculator
def printline():
    print("-----------------------------------------")
#Print een lijn.


Smallpiza = 2.49
Smallpizasold = input("Hoeveel kleine pizzas wilt u?\n")
# smallpiza = kosten.
# Smallpizasold verkocht aantal.

printline()

Medpizza = 5.49
Medpizzasold = input("Hoeveel medium pizzas wilt u?\n")

printline()

LargePizza = 7.43
Largepizzadsold = input("Hoeveel grote pizzas wilt u?\n")

for i in range(100):
    print("")

eurospizzaklein = (int(Smallpizasold) * Smallpiza)
centenpizzaklein = round((eurospizzaklein - int(eurospizzaklein)) * 100)
print(f"Er zijn {Smallpizasold} kleine pizza's verkocht.")
print(f"dat heeft gezorgd voor een opbrengst van {int(eurospizzaklein)} euro en {round(centenpizzaklein, 2)} eurocent van kleine pizzas.\n")
# 1 verkochte pizza * prijs.
# centen in variabel omgezet.
# in regel 3 en 4 wordt de informatie geprint.

eurospizzamed = (int(Medpizzasold) * Medpizza)
centenpizzamed = round((eurospizzamed - int(eurospizzamed)) * 100)
print(f"Er zijn {Medpizzasold} medium pizza's verkocht.")
print(f"dat heeft gezorgd voor een opbrengst van {int(eurospizzamed)} euro en {round(centenpizzamed, 2)} eurocent van medium pizzas.\n")

eurospizzalarge = (int(Largepizzadsold) * LargePizza)
centenpizzalarge = round((eurospizzalarge - int(eurospizzalarge)) * 100)
print(f"Er zijn {Largepizzadsold} medium pizza's verekocht.")
print(f"dat heeft gezorgd voor een opbrengst van {int(eurospizzalarge)} euro en {round(centenpizzalarge, 2)} eurocent van medium pizzas.\n")

totalewinst = (eurospizzaklein + eurospizzamed + eurospizzalarge)
totalecenten = round((totalewinst - int(totalewinst)) * 100)

print(f"In totaal heeft de pizzamaker een winst van {round(totalewinst)} euro en {round(totalecenten, 2)} cent.")

# in regel 38 worden alle bedragen bij elkaar opgeteld.


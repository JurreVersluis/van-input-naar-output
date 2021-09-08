croissantjes = 17.0
kosten1 = 0.39
stokbroden = 2.0
kosten2 = 2.78
korting = -1.50
dekosten = kosten1 * croissantjes + stokbroden * kosten2 + korting
centen = round((dekosten - int(dekosten)) * 100)
print(f"De feestlunch kost je bij de bakker {int(dekosten)} euro en {(centen)} voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")
print(f"dat is dus {int(dekosten) * 100 + (centen)} eurocent.")
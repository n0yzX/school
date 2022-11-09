brutto = float(input("Geben Sie den Brutto Betrag ein: "))
rabattinput = float(input("Geben Sie den gegebenen Rabatt ein: "))


neuBrutto = brutto-(brutto/100)*rabattinput
steuer = ((neuBrutto/119)* 19)
netto = neuBrutto - steuer


print("Der Neue Brutto nach Rabatt:",neuBrutto)
print("Davon 19% MwSt:",steuer)
print("Netto:",netto)

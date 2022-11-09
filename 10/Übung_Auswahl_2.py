dienstjahre =int(input("Dienstjahre: \n"))
alter = int(input("Alter: \n"))
bonus = 0

if dienstjahre < 1 :
    bonus = 0

if dienstjahre >= 1 and dienstjahre < 6 :
    bonus = 200
    
if dienstjahre >6 :
    bonus = 80 + (dienstjahre * 20)
    if alter >= 50 :
        bonus = bonus + 50


print("Der Bonus Beträgt:{}" .format(bonus))
    
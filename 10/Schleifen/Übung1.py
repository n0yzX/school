import random

# Aufgabe 1
sum = 0

for i in range(1,101):
    sum +=i

print(sum)

# Aufgabe 2
intervall_start2 = random.randint(1, 100)
intervall_ende2 = random.randint(1, 100)
sum2 = 0

if intervall_start2 > intervall_ende2:
        print("Ungültiges Intervall")

else:    
    for i in range(intervall_start2, intervall_ende2+1):
        sum2 +=i
print(sum2)

# Aufgabe 3

intervall_start3 = random.randint(1, 100)
intervall_ende3 = random.randint(1, 100)
sum3 = 0

if intervall_start3 > intervall_ende3:
    print("Ungültiges Intervall")
    
else:
    while intervall_start3 < intervall_ende3:
        sum3 = sum3 + intervall_start3
        intervall_start3 +=1

print(sum3)

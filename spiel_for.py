#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Schleife mit for und Eingabe
for i in 1, 2, 3, 4:
    print("Bitte eine Zahl eingeben:")
    z = input()
    zahl = int(z)

#Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        break
    else:
        print(zahl, "ist falsch")


#Ende
print("Ergebnis: ", c)

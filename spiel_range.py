#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Schleife mit range
for tries in range(1,10):
    print("Bitte eine Zahl eingeben: ")
    z = input()
    zahl = int(z)
    if zahl == c:
        print(zahl, "ist richtig")
        break
    else:
        print(zahl, "ist falsch")
print("Ergebnis: ", c)
print("Anzahl der Versuche: ", tries)

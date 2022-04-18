#Zufallsgenerator
import random
random.seed()

#Werte der Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe: ", a, "+", b)

#Schleife und Anzahl initialisieren
zahl = c + 1
versuch = 0

#Schleife mit while
while zahl != c:
    versuch = versuch + 1
    print("Bitte eine ganze Zahl eingeben:")
    z = input()

    try:
        zahl = int(z)
    except:
        print("Sie haben keine ganze Zahl eingegeben")
        continue
    if zahl == c:
        print(zahl, "ist richtig")
    else:
        print(zahl, "ist falsch")

print("Ergebnis: ", c)
print("Anzahl Versuche:", versuch)

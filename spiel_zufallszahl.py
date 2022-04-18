#Modul random importieren
import random

#Zufallsgenerator initialisieren
random.seed()

#Zufallswerte un Berechnung
a = random.randint(1,100)
b = random.randint(1,100)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Eingabe
print("Bitte eine Zahl eingeben:")
z = input()
zahl = int(z)

#Ausgabe
print("Ihre Eingabe:", z)
print("Das Ergebnis:", c)

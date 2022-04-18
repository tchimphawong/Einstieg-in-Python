#Aufgabe
def aufgabe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    erg = a + b
    print("Die Aufgabe: ", a, "+", b)
    return erg

def kommentar(eingabezahl, ergebnis):
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig")
    else:
        print(eingabezahl, "ist falsch")

#Zufallsgenerator
import random
random.seed()

#Aufgabe
c = aufgabe()

#Schleife und Anzahl initialisieren
zahl = c + 1
versuch = 0

#Schleife mit while
while zahl != c:
    versuch = versuch + 1
    print("Bitte eine Zahl eingeben: ")
    z = input()

    try:
        zahl = int(z)
    except:
        print("Sie haben keine Zahl eingegeben")
        continue

    kommentar(zahl,c)

print("Ergebnis: ", c)
print("Anzahl Versuche: ", versuch)

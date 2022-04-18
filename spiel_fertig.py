#1.Zufallsgenerator
import random
random.seed()

#2 Anzahl Aufgaben
anzahl = -1
while anzahl<0 or anzahl>10:
    try:
        print("Wie viele Aufgaben (1 bis 10):")
        anzahl = int(input())
    except:
        continue

#Anzahl richtige Ergebnisse
richtig = 0

#Schleife mit "anzahl" Aufgaben
for aufgabe in range(1,anzahl+1):
    #5 Operatorauswahl
    opzahl = random.randint(1,4)
    #Operandenauswahl
    if(opzahl == 1):
        a = random.randint(-10,30)
        b = random.randint(-10,30)
        op = "+"
        c = a + b
    elif(opzahl == 2):
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "-"
        c = a - b
    elif(opzahl == 3):
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = "*"
        c = a * b
    #Sonderfall Division
    elif(opzahl == 4):
        c = random.randint(1,10)
        b = random.randint(1,10)
        op = "/"
        a = c * b
#Aufgabenstellung
    print("Aufgabe", aufgabe, "von", anzahl, ":", a, op, b)

#9 Schleife mit 3 Versuchen
    for versuch in range(1,4):
        try:
            print("Bitte eine Zahl eingeben:")
            zahl = int(input())
        except:
            print("Sie haben keine Zahl eingegeben")
            continue
        if zahl == c:
            print(zahl, "ist richtig")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch")
    print("Ergebnis: ", c)
    print("Richtig:", richtig, "von", anzahl)

#Eingabe
print("Bitte geben Sie eine ganze Zahl ein")
z = input()

#Versuch der Umwandlung
try:
    zahl = int(z)
    print("Sie haben die ganze Zahl", zahl, "richtig eingegeben")

#Fehler bei Umwandlung
except:
        print("Sie haben die ganze Zahl nicht richtig eingegeben")

print("Ende des Programms")

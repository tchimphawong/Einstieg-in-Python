#Initialisierung der while-Schleife
fehler = 1
#Schleife bei falscher Eingabe
while fehler == 1:
    print("Bitte geben Sie eine ganze Zahl ein")
    z = input()

    try:
        zahl = int(z)
        print("Sie haben die ganze Zahl", zahl,"richtig eingegeben")
        fehler = 0
    except:
        print("Sie haben die ganze Zahl nicht"
              " richtig eingegeben")
print("Ende des Programms")

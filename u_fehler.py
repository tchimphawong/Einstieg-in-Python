#Definition
e = 1

#While Schleife und ErrorValue abfang
while e == 1 :
    print("Geben Sie den Inch-Wert ein: ")
    i = input()

    try:
        inch = float(i)
        print(inch*2.54,"cm")
        e = 0
    except:
        print("Falsche Eingabe")

print("Ende des Programms")

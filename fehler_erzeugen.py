# Wiederholung Eingabe
fehler = True
while fehler:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl < 0:
            raise
        kw = 1.0 / zahl
        fehler = False
    except:
        print("Fehler")

# Augabe
print("Der Kehrwert von", zahl, "ist", kw)

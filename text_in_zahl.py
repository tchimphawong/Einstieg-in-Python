# Erste Zeichenkette
x = "15.3"

ergebnis = x * 2
print(ergebnis)

x = float(x)
ergebnis = x * 2
print(ergebnis)

#Zweite Zeichenkette
x = "17"
ergebnis = x * 2
print(ergebnis)

x = int(x)
ergebnis = x * 2
print(ergebnis)

#Fehler abfangen
x = "15.3p"

try:
    x = float(x)
    print(x*2)
except:
    print("Zeichenkette kann nicht umgewandelt werden")

# Tupel mit und ohne Klammer
z = (3, 6, -8, 5.5)
print("Tupel 1:", z)

z = 6, 8, -3
print("Tupel 2:", z)

# mehrdimensionale Tupel, unterschiedliche Objekte
x = (("Paris","F",3500000), ["Rom","It", 4200000])
print("mehrdim. Tupel:")
print(x)

#Ersetzen
try:
    x[0][0] = "Lyon"
except:
    print("Fehler")
    x[1][0] = "Pisa"
    print("Listenelement ersetzt:", x[1])

#Tupel bei for-Schleife
for i in 4, 5, 12:
    print("i:", i)

#Zuweisung mit Tupel
x,y = 2,18
print("x:", x, "y:", y)

# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return self.bezeichnung + " " \
               + str(self.geschwindigkeit) + " km/h"
    def __repr__(self):
        return "Objekt " + self.bezeichnung \
               + " der Klasse Fahrzeug"

# Objekt der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)

# objekte ausgeben
print(opel)
print(volvo)

# Informationen zu Objekt
print(repr(opel))
print(repr(volvo))

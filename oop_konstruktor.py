# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __del__(self):
        print("Objekt", self.bezeichnung, "entfernt")
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
        self.ausgabe()
    def ausgabe(self):
        print(self.bezeichnung, self.geschwindigkeit, "km/h")

# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)

# Ojekte betrachten
opel.ausgabe()
volvo.ausgabe()

# Objektmethode
volvo.beschleunigen(20)

# Destruktor
del opel
del volvo

# Aufruf nicht mehr gestattet
# opel.ausgabe()

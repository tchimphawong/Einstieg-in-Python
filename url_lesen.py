import sys, urllib.request

# verbindung zu einer URL
try:
    u = urllib.request.urlopen \
        ("http://localhost/Python36/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines(0)

# Schließt die Verbindung
u.close()

# Ausgabe der Liste

for element in li:
    print(element)

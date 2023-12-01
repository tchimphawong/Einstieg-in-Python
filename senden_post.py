import urllib.request, urllib.parse

# Eingabedaten

pnn = input("Bitte Nachnamen eingeben: ")
pvn = input("Bitte Vornamen eingeben: ")

# Dictionary mit Sendedaten, Codierung

dc = {b"nn":pnn, b"vn":pvn}
data = bytes(urllib.parse.urlencode(dc), "UTF-8")

# sendet Daten
u = urllib.request.urlopen \
    ("http://localhost/Python36/senden_post.php", data)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
for element in li:
    print(element)

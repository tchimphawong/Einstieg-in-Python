# Modul Time
import time

# zeitangabe erzeugen
dztupel = 1979, 2, 15, 13, 0, 0, 0, 0, 0
print(time.strftime("%d.%m.%Y %H:%M:%S", dztupel))
damals = time.mktime(dztupel)

# Ausgabe
lt = time.localtime(damals)

# Wochentag
wtage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
         "Freitag", "Samstag", "Sonntag"]
wtagnr = lt[6]
print("Dast ist ein", wtage[wtagnr])

# Tag des Jahres
tag_des_jahres = lt[7]
print(f"Der {tag_des_jahres:d}. Tag des Jahres")

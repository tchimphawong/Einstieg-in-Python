import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfragen
# Einzelne Felder

sql = "SELECT name, vorname FROM personen"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Auswahl mit WHERE-Klausel und Vergleichsoperator
sql = "SELECT * FROM personen " \
      "WHERE gehalt > 3600"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

# Auswahl der Zeichenkette
sql = "SELECT * FROM personen " \
      "WHERE name = 'Schmitz'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Auswahl mit logischen operatoren
sql = "SELECT * FROM personen " \
      "WHERE gehalt >= 3600 AND gehalt <= 3650"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

# Verbindung beenden
connection.close()

import os, sys, sqlite3

datenbank_pfad = "firma.db"

if os.path.exists(datenbank_pfad):
    os.remove(datenbank_pfad)
    print("Datenbank gelöscht.")
else:
    print("Die Datenbankdatei existiert nicht.")
print()

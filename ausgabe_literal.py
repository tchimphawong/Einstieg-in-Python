# Zahl mit Nachkommastellen
x = 100/7
y = 2/7
print("Zahlen", x, y)
print()

# FOrmat f
print(f"Format f, Standart:   {x:f} {x:f} {y:f}")
print(f"Format f, nach Komma: {x:.25f}")
print(f"Format f, gesamt: {x:15.10f}")
print()

#Format e
print(f"Format e, Standart:   {x:e}")
print(f"Format e, nach Komma: {x:.3e}")
print(f"Format e, gesamt: {x:12.3e}")
print()

#Format %
print(f"Format %, Standart:  {y:%}")
print(f"Format %, nach Komma: {y:.3%}")
print(f"Format %, gesamt:   {y:12.3%}")
print()



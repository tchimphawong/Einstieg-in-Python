# Modul
import collections

# Neu erzeugen
d = collections.deque([8, 18, 28])
print("Neu erzeugt:", d)

# Einzelne Elemente angefügt
d.appendleft(5)
d.append(25)
print("Einzelne Elemente angefügt:", d)

# Einzelne Elemente eingefügt
d.insert(2, 11)
print("Einzelne Elemt eingefügt:", d)

# Um mehrere Elemente erweitert
d.extend([7, 9])
d.extend([17,19])
print("Um mehrere Elemente erweitert:", d)

# Element suchen
try:
    print("Position des Werts 5:", d.index(5))
except:
    print("Wert 5 nicht vorhanden")

# Einzelne Elemente entfernen
for i in range(5):
    li = d.popleft()
    print("Entferntes Element, links:", li)
re = d.pop()
print("Entferntes Element, rechts:", re)
print("Nach Entfernung:", d)

# Deque intern rotieren lassen
d.rotate()
print("Nach Rotation um +1:", d)
d.rotate(-1)
print("Nach Rotation um -1:", d)
    
    
    

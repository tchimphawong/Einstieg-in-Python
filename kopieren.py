# Modul copy
import copy

#Kopie einer Liste, Methode 1
x = [23,"hallO",-7.5]
y = []
for i in x:
    y.append(i)
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

#Kopie einer Liste, Methode 2
x = [23,["Berlin","Hamburg"],-7.5,12,67]
y = copy.deepcopy(x)
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)

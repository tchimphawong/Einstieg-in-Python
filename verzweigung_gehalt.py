#Steuerbeträge prozent und Gehalt in Euro
tax1 = 0.18
tax2 = 0.22
salary = 2500

#Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein: ")
z = input()
pay = float(z)

#Rechnung
taxlow = pay * tax1
taxhigh = pay * tax2

#Verzweigung
if pay <= 2500:
    print("Es ergibt sich ein Steuerbetrag von",taxlow,"Euro")
else:
    print("Es ergibt sich ein Steuerbetrag von",taxhigh,"Euro")

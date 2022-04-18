#Steuerbeträge prozent und Gehalt in Euro
taxlow = 0.18
taxhigh = 0.22
salary = 2500

#Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein: ")
z = input()
pay = float(z)

#Verzweigung und Rechnung
if pay <= 2500:
    print("Es ergibt sich ein Steuerbetrag von", pay * taxlow,"Euro")
else:
    print("Es ergibt sich ein Steuerbetrag von", pay * taxhigh,"Euro")

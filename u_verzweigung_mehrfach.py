#Steuerbeträge prozent
tax1 = 0.18
tax2 = 0.22
tax3 = 0.26

#Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein: ")
z = input()
pay = int(z)

#Rechnung
taxlow = pay * tax1
taxmid = pay * tax2
taxhigh = pay * tax3

#Verzweigung
if pay <= 2500:
    print("Es ergibt sich ein Steuerbetrag von",taxlow,"Euro")
elif pay <= 4000:
    print("Es ergibt sich ein Steuerbetrag von",taxmid,"Euro")
else:
    print("Es ergibt sich ein Steuerbetrag von",taxhigh,"Euro")

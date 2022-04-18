#Steuerbeträge prozent und verheiratet
tax1 = 0.18
tax2 = 0.22
tax3 = 0.26

#Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein: ")
pay = int(input())
print("Geben Sie Ihr Familienstatus ein:")
print("1 = ledig 2 = verheiratet")
fs = int(input())
#Rechnung
taxlow = pay * tax1
taxmid = pay * tax2
taxhigh = pay * tax3

#Verzweigung
if pay <= 2500:
    print("Es ergibt sich ein Steuerbetrag von",taxlow,"Euro")
elif pay <= 4000 and fs==1:
    print("Es ergibt sich ein Steuerbetrag von",taxlow,"Euro")
elif pay <= 4000 and fs==2:
    print("Es ergibt sich ein Steuerbetrag von",taxmid,"Euro")
elif pay > 4000 and fs==1:
    print("Es ergibt sich ein Steuerbetrag von",taxmid,"Euro")
elif pay > 4000 and fs==2:
    print("Es ergibt sich ein Steuerbetrag von",taxhigh,"Euro")
else:
    print("Steuerbetrag konnte nicht errechnet werden!")

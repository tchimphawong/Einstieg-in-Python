import u_modul_finanz as umz

#Eingabe
fehler = 1
print("Geben Sie ihr Bruttogehalt ein: ")
while fehler != 0:
    try:
        stbr = float(input())
        print("Ihr Steuerbetrag: ", umz.steuer(stbr))
        fehler = 0
    except:
        print("Sie haben keine Zahl eingegeben")
        print("Geben Sie Ihr Bruttogehalt ein: ")
        continue

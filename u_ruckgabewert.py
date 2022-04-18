def steuer(x):
    if x >= 2500:
        stb = x*0.22
    else:
        stb = x*0.18
    return stb
        

#Eingabe
fehler = 1
print("Geben Sie ihr Bruttogehalt ein: ")
while fehler != 0:
    try:
        stbr = float(input())
        print("Ihr Steuerbetrag: ", steuer(stbr))
        fehler = 0
    except:
        print("Sie haben keine Zahl eingegeben")
        print("Geben Sie Ihr Bruttogehalt ein: ")
        continue

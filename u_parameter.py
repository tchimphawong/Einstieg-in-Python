def steuer(x):
    if x >= 2500:
        print("Ihr Steuerbetrag: ", x*0.22)
    else:
        print("Ihr Steuerbetrag: ", x*0.18)

#Hauptprogramm
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)

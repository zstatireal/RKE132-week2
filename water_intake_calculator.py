# Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
# Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
# Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“
# üks klaas == 250ml vett

kogus = int(input("Kui palju klaase vett sa joonud oled?"))
kogus = kogus*250
kogus = kogus/2000*100

if kogus < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif kogus < 100:
    print("Tubli, jätka samas vaimus!")
elif kogus >= 100:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
else:
    print("error")
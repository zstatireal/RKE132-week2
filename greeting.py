# Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
# Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
# Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“

pere = input("Mis on su perekonnanimi?")
sugu = input("Kas sa oled Mees või Naine? (vali 'm' või 'n')")

if sugu == "m":
    print("Tere, härra " + pere +"")
elif sugu == "n":
    print("Tere, proua " + pere + "")
else:
    print("Tere tulemast, " + pere + "!")

def goedemorgen(naam, totziens=True):
    print("Goedemorgen", naam)
    if totziens:
        print("Tot ziens!")


goedemorgen("Martijn")

goedemorgen("Amber", False)

goedemorgen(totziens=False, naam="Valentin")

goedemorgen(totziens=True, naam="Sayed")
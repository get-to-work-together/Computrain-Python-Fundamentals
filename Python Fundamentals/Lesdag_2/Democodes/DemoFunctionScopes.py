#bmi = 1
def bereken_bmi(gewicht, lengte):
    global bmi
    bmi = gewicht / lengte**2
    return bmi

def toonBMIgegevens():
    print(bmigewicht)
    print(bmihoogte)
    print(bmi)

bmigewicht = 100
bmihoogte = 1.8

bereken_bmi(bmigewicht, bmihoogte)

toonBMIgegevens()

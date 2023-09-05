import math

def pizza(halkasia, hinta):
    pinta_ala = math.pi / 4 * halkasia ** 2
    return hinta / (pinta_ala / 10000)

sade1 = int(input("Pizzan halkasia senttimetreinä?: "))
hint1 = int(input("Pizzan hinta euroina?: "))

sade2 = int(input("Pizzan halkasia senttimetreinä?: "))
hint2 = int(input("Pizzan hinta euroina?: "))

pizzan_kokonaishinta1 = pizza(sade1, hint1)
pizzan_kokonaishinta2 = pizza(sade2, hint2)

if pizzan_kokonaishinta1 < pizzan_kokonaishinta2:
    print("Ensimmäinen pizza on halvempi")
else:
    print("Toinen pizza on halvempi")

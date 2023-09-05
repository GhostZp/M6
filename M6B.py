import random

kulma = int(input("Kuinka monta kulmaa nopassa?: "))
def noppa(yhteismaara):
    numero = (random.randint(1, yhteismaara))
    return numero

while True:
    nopat = noppa(kulma)
    print(f"{nopat}")
    if nopat == kulma:
        break

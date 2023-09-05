import random

def noppa():
    numero = (random.randint(1, 6))
    return numero

while True:
    nopat = noppa()
    print(f"{nopat}")
    if nopat == 6:
        break

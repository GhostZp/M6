
def luku(luvut):
    parittomat = []
    for luku in luvut:
        if luku % 2 == 0:
            parittomat.append(luku)
    return parittomat

luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(luvut)
print(luku(luvut))

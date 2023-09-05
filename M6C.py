
def bensa(gallo):
    return gallo * 3.785

while True:
    gallo = int(input(f"Kerro galloona määrä: "))

    if gallo < 0:
        break
    print(f"{bensa(gallo)} litraa.")

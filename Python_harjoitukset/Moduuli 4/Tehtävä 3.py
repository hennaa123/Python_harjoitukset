syöte = input ("Anna luku:")
pienin = none
suurin = none

while syöte != "":
    luku=float(syote)

    if pienin is Nonre or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
    syote = input("Anna luku:")
print("Pienin luku:", pienin)
print("Suurin luku:", suurin)

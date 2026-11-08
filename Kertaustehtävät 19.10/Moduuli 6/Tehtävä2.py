import random
def heita_noppaa(tahkot):
    return random.randint(1,tahkot)

tahkot = int(input("Anna nopean tahkojen määrä"))
silmäluku = 0

while silmäluku !=tahkot:
    silmaluku = heita_noppaa(tahkot)
    print(silmaluku)

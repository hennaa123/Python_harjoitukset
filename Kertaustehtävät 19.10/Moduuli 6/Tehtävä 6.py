import match

def pizzan_hinta(halkaisija, hinta):
    sade = halkaisija / 200
    pinta_ala = match.pi * sade ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija:"))
hinta1 = float(input("Anna ensimmäisen pitsan hinta:"))

halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2= float(input("Anna toisen pizzan hinta:"))

pizza1 = pizzan_hinta(halkaisija1, hinta1)
pizza2 = pizzan_hinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta:", round (pizza1, 2))
print("Toisen pizzan yksikköhinta:", round (pizza 2, 2))

if pizza1 < pizza2:
    print("Ensimmäinen pizza on edullisempi.")
else:
    print("Toinen pizza on edullisempi.")
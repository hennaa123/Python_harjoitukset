leiviskät = int(input("Anna leiviskät"))
naulat = int(input("Anna naulat"))
luodit = float(input("Anna luodit"))
luodit_yhteensä = leiviskät *20 *32 +naulat *32 + luodit
grammat= luodit_yhteensä * 13.3
kilogrammat = int (grammat //1000)
grammat_jaljella = grammat % 1000
print("massa =",kilogrammat, "kg ja", grammat_jaljella, "g")

import random
koodi1 = ""
koodi2 = ""
for i in range (3):
   koodi1 = koodi1 + str (random.randint(0, 9))
for i in range (4):
   koodi2 = koodi2 + str(random.randint(1, 6))
print ("kolminumeroinen koodi:", koodi1)
print ("nelinumeroinen koodi:", koodi2)

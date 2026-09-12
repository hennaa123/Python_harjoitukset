import random
koodi1 = ""
koodi2 = ""
for i in range (3):
   koodi1 = koodi1 + str (random.randint(0, 9))
for i in range (4):
   koodi2 = koodi2 + str(random.randint(1, 6))
print ("kolminumeroinen koodi:", koodi1)
print ("nelinumeroinen koodi:", koodi2)

#Tunnilla 10.9 tehty toinen versio:

import random
num1 = random.randit (1,6)
num2 = random.randit (1,6)
num3 = random.randit (1,6)
num4 = random.randit (1,6)
print(f"koodi on:{num1}{num2}{num3}{num4}")

sukupuoli=input("Anna sukupuolesi mies/nainen:")
hemoglobiini=float(input("Anna hemoglobiiniarvo:"))
if sukupuoli == "nainen":
   if hemoglobiini < 117:
      print("hemoglobiiniarvo on liian alhainen.")
   elif hemoglobiini <=175:
       print("hemoglobiiniarvo on normaali.")
   else:
        print("hemoglobiiniarvo on korkea.")

if sukupuoli == "mies":
   if hemoglobiini <134:
      print ("hemoglobiini on liian alhainen.") 
   elif hemoglobiini <=195:
          print ("hemoglobiini on normaali.")
   else:
        print ("hemoglobiini on korkea.")



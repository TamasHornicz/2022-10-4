import math
szam1 = int(input("Írja be az első számot: "))
szam2 = int(input("Írja be a második számot: "))
szam3 = int(input("Írja be a harmadik számot: "))


if((szam1 <= szam2) and (szam1 <= szam3)):
    print ("Az első szám a legkissebb")
elif((szam2 <= szam3) and (szam2 <= szam1)):
    print ("A második szám a legkissebb")
else:
    print("A harmadik szám a legkissebb")


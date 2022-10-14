import math 
a = int(input("Adja meg a fal magasságát: "))
b = int(input("Adja meg a fal szélességét: "))

T=a*b

csempe =0.2**2
darabszam = T/csempe
szazalek =darabszam/100*10
vege = math.ceil(darabszam + szazalek)

print(vege)
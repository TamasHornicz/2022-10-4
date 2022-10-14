import random


pc= random.randint(1,3)
print("Választásod:(1-kő 2-papír 3-olló)")
v=int(input())


if(pc==v):
    print("Döntetlen")
elif((v==1) and (pc==3) or (v==2) and (pc==1) or (v==3) and (v==2)):
    print("user nyert")
else:
    print("Gép nyert")

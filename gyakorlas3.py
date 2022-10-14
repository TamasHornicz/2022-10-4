import random


nev1=input("Első játékos neve: ")
nev2=input("Második játékos neve: ")

print(nev1," játékos dob (ENTER)")
input()
user1 = random.randint(1,6)
print("Dobása: ",user1)
print(nev2," játékos dob (ENTER)")
input()
user2 = random.randint(1,6)
print("Dobása:",user2)




if(user1> user2):
    print(nev1,"nyert")
elif(user1 < user2):
    print(nev2, "nyert")
else:
    print("Döntetlen")
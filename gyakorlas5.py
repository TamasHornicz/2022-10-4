penz = int(input("Írjon be a kifizetendő összeget: "))


print("20000Ft :",penz//20000,"db")
maradek=penz%20000
print("10000Ft :",maradek//10000,"db")
maradek=maradek%10000
print("5000Ft :",maradek//5000,"db")
maradek=maradek%5000
print("2000Ft :",maradek//2000,"db")
maradek=maradek%2000
print("1000Ft :",maradek//1000,"db")
maradek=maradek%1000
print("500Ft :",maradek//500,"db")
maradek=maradek%500
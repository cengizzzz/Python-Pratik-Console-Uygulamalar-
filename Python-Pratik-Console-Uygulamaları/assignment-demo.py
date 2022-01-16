x, y, z = 2, 5, 107
numbers=1, 5, 7, 10, 6

# a=int(input("Birinci Sayıyı Girin : "))
# b=int(input("İkinci Sayıyı Girin : "))
# carpim=a*b
# toplam=x+y+z
# fark=carpim-toplam
# print(fark)

# kalansız=y//x
# print(kalansız)

# toplam=x+y+z
# print(toplam%3)

# kuvvet=y**x
# print(kuvvet)

x,*y,z=numbers
print("Z nin Küpü :",z**3)
print("Y değerlerinin Toplamı :",y[0]+y[1]+y[2])
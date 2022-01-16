
sayilar=[1,3,5,7,9,12,19,21]

# i=0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i +=1

# start=int(input("Başlangıç değerini giriniz :"))
# finish=int(input("Bitiş değerini giriniz :"))
# while (start<=finish):
#     if start % 2!=0:
#         print(f"{start} Tek sayıdır")
#     start +=1

# i=100
# while (i>=0):
#     print(i)
#     i -=1

# i=1
# sayilar=[]
# while i <= 5:
#     sayi=int(input("Sayıları giriniz :"))
#     sayilar.append(sayi)
#     i +=1
# sayilar.sort()
# print(sayilar) 

urunler=[]
urun_sayi=int(input("Ürün sayısını giriniz :"))
i=1
while (i<=urun_sayi):
    name=input("Ürün ismi :")
    price=int(input("Ürün Fiyaı :"))
    urunler.append({
        "name":name,
        "price":price
    })
    i +=1
i=1
for urun in urunler:
    print(urun)




from sre_constants import RANGE, error


liste=["1","2","5a","10b","abc","10","50"]

# for x in liste:
#     try:
#         result=int(x)
#         print(x)
#     except Exception as hata:
#         print(hata)

# while True:   
#     x=input("Sayı Gir : ")
#     if  x == 'q' :
#         break
#     try:
#         result=int(x)
#         print("Girilen sayı : ",x)
#     except Exception as hata:
#         print("Sayı değeri giriniz!",hata)
#         continue
        
# def parola_kontrol(parola): 
#     turkce_karakterler="ığüşçöİĞÜŞÇÖ"   
#     for i in parola:
#         if i in turkce_karakterler:
#             raise Exception("Parola türkçe karakter içeremez!")
#         else:
#             pass
# while True:
#     try:
#        parola=input("Parola Giriniz : ")
#        parola_kontrol(parola)
#     except:
#        print("hatalı parola Giriniz")
#     else:
#         print("Parola Başarılı")
#         break

def faktoriyel_al(deger):
    last=1
    if deger<0:
            raise Exception("Negatif değer girilemez!")
    for i in range(1,deger+1):
        last=last*i
    print("Faktöriyeli : ",last)


while True:
    try:
        deger=int(input("Sayi Gir : "))
        faktoriyel_al(deger)
        result=int(deger)       
    except Exception as hata:
        print("Gelen değer sayi değil!", hata)
    else:
        break

    
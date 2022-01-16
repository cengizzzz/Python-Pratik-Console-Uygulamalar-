ogrenciler={}

# number=input("Öğrenci no : ")
# name=input("Öğrenci Adi : ")
# surname=input("Öğrenci Soyadı : ")
# phone=input("Öğrenci Tel No : ")
# ogrenciler[number]={
#     "Ad":name,
#     "Soyad":surname,
#     "Phone":phone
# }
# number=input("Öğrenci no : ")
# name=input("Öğrenci Adi : ")
# surname=input("Öğrenci Soyadı : ")
# phone=input("Öğrenci Tel No : ")
# ogrenciler[number]={
#     "Ad":name,
#     "Soyad":surname,
#     "Phone":phone
# }
number=input("Öğrenci no : ")
name=input("Öğrenci Adi : ")
surname=input("Öğrenci Soyadı : ")
phone=input("Öğrenci Tel No : ")
ogrenciler[number]={
    "Ad":name,
    "Soyad":surname,
    "Phone":phone
}
print(ogrenciler)
print("*"*50)
ogr_no=input("Öğrenci no Gir: ")
ogrenci=ogrenciler[ogr_no]
print("*"*50)
print(f"Aradığınız {ogr_no} nolu ögrencinin adı : {ogrenci['Ad']} soyadı: {ogrenci['Soyad']} numarası: {ogrenci['Phone']}")
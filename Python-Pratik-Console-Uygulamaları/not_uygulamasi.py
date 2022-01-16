def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")

    ogrenci_ad=liste[0]
    ogrenci_not=liste[1]
    ogrenci_not=liste[1].split(",")

    not1=int(ogrenci_not[0])
    not2=int(ogrenci_not[1])
    not3=int(ogrenci_not[2])

    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf ="AA"
    elif ortalama>=50 and ortalama<=89:
        harf ="BB"
    else:
        harf ="FF"
    return ogrenci_ad + " : " + harf+ "\n"

def ortalamalari_oku():
    with open("newfile.txt","r",encoding="utf8")as file:
        for satir in file:
            print(not_hesapla(satir))    

def notlari_kayitet():
    with open("newfile.txt","r",encoding="utf-8")as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8")as file2:
            for i in liste:
                file2.write(i)

def not_gir():
    ad=input("Öğrenci Adı: ")
    soyad=input("Öğrenci Soyad: ")
    not1=input("Öğrenci Not1: ")
    not2=input("Öğrenci Not2: ")
    not3=input("Öğrenci Not3: ")
    with open("newfile.txt","a",encoding="utf-8")as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")

while True: 
    islem=input("1- Notları Oku\n2- Not gir\n3- Notları Kayıt et\n4- Çıkış\n")
    if islem=="1":
        ortalamalari_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notlari_kayitet()
    else:
        break
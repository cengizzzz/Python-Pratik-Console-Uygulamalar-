import datetime
# isim=input("İsim giriniz :")
# yas=int(input("Yaş Giriniz :"))
# egitim_bilgi=input("Eğitim bilgilerinizi giriniz :")

# if(yas>=18) and (egitim_bilgi=="lise"):
#     print(f"{isim} Ehliyet alabilir :)")
# elif(egitim_bilgi=="üniversite"):
#     print(f"{isim} Ehliyet alabilir :)")
# else:
#     print(f"{isim} Ehliyet almak için uygun değildir :(")

# not1=int(input("Birinci Notu Gir :"))
# not2=int(input("İkinci Notu Gir :"))
# sozlu=int(input("Sozlu Notunu Gir :"))
# result=(not1+not2+sozlu)/3
# if(result>=0 and result<=24):
#     print("0")
# elif(result>=25 and result<44):
#     print("1")
# elif(result>=45 and result<54):
#     print("2")
# elif(result>=55 and result<69):
#     print("3")
# elif(result>=70 and result<84):
#     print("4")
# elif(result>=85 and result<=100):
#     print("5")

# tarih=input("Aracımız hangi tarihte trafige çıkmıştır (2021/7/17)  :")
# tarih=tarih.split('/')
# print(tarih)
# trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# suan=datetime.datetime.now()
# fark=suan-trafigecikis
# print(fark.days)
# if(fark.days<=365):
#     print("1. bakım yılı")
# elif(fark.days<=365*2):
#     print("2. bakım yılı")
# elif(fark.days<=365*3):
#     print("3. bakım yılı")
# else:
#     print("hatalı tarih")
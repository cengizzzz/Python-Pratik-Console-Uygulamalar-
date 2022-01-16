sayilar=[1,3,5,7,9,12,19,21]
# for sayi in sayilar:
#     if (sayi % 3==0):
#         print(f"{sayi} Üçün katıdır.")
#     else:
#         print("Üçün katı değildir.")

# toplam=0
# for sayi in sayilar:
#     toplam=toplam+sayi
# print(f"Sayıların toplamı: {toplam}")

# for sayi in sayilar:
#     if sayi % 2!=0:
#         kare=sayi**2
#         print(f"{sayi}'in karesi :",kare)

# sehirler=["kocaeli","istanbul","ankara","izmir","tokat","rize"]
# for sehir in sehirler:
#     if (len(sehir) <= 5):
#         print(f"{sehir} en fazla 5 karakterldir")

# urunler=[
#     {"name":"samsung s6","prince":"3000"},
#     {"name":"samsung s7","prince":"4000"},
#     {"name":"samsung s8","prince":"5000"},
#     {"name":"samsung s9","prince":"6000"},
#     {"name":"samsung s10","prince":"7000"}
# ]
# toplam=0
# for urun in urunler:
#     fiyat=int(urun["prince"])
#     toplam +=fiyat
# print(toplam)

# toplam=0
# for urun in urunler:
#     if (int(urun["prince"]) <= 5000):
#         print(urun["name"])
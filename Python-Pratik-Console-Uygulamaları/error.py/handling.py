# try:
#     x=int(input("x :"))
#     y=int(input("y :"))
#     print(x/y)
# except(ZeroDivisionError,ValueError) as hata:
#     print("Yanlış Bilgi Girdiniz..")
#     print("Hata Tanımlaması : " , hata)
# else:
#     print("Herşey yolunda :)")


while True:
         try:
            x=int(input("x :"))
            y=int(input("y :"))
            print(x/y)
         except(Exception) as hata:
            print("Yanlış Bilgi Girdiniz..")
            print("Hata Tanımlaması : " , hata)
         else:
             break
         finally:
             print("Try except sonlandı. ")

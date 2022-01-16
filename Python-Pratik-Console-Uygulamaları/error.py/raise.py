# x=10

# if x>5:
#     raise Exception("x 5 den büyük olamaz")

def parola_kontrol():
    import re #istediğimizi aratma metodu
    while True:
        try:
            parola=input("Parola giriniz :")
            if len(parola)<8:
               raise Exception("Parola en az 8 karakter olmalıdır!")
            elif not re.search("[a-z]",parola):
               raise Exception("Parola küçük harf içermelidir!")
            elif not re.search("[A-Z]",parola):
               raise Exception("Parola büyük harf içermelidir!")
            elif not re.search("[0-9]",parola):
               raise Exception("Parola rakam içermelidir!")
            elif not re.search("[_@$]",parola):
               raise Exception("Parola alpha numeric karakter içermelidir!")
            elif re.search("\s",parola):
               raise Exception("Parola boşluk içermemelidir!")
            else:
                print("Parola Başarılı :)")
        except Exception as hata:
             print(hata)
        else:
            break

parola_kontrol()



    
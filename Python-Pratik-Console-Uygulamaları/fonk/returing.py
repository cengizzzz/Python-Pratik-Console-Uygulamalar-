# def yetki_sorgula(page):
#     def inner(role):
#         if role=="Admin":
#             return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
#     return inner

# user1=yetki_sorgula("sayfa girişi")
# print(user1("Admin"))
# print(user1("editör"))


def islem(islem):
    def topla(*argm):
        toplam=0
        for i in argm:
            toplam+=i
        return toplam
    def carpma(*argm):
        carpma=1
        for i in argm:
            carpma*=i
        return carpma
    if islem=="topla":
        return topla
    else:
        return carpma

yap=islem("carpma")
print(yap(1,2,3,5,6))
yap=islem("topla")
print(yap(1,5,9,8,7,6,3,4))
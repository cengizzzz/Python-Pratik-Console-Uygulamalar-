cengiz= {
    "ad" : "Cengiz ATİLA,",
    "hesapNo" : "1234",
    "bakiye" : 3000,
    "ekHesap": 2000
    }
atila= {
    "ad" : "Cengiz ATİLA,",
    "hesapNo" : "1234",
    "bakiye" : 3000,
    "ekHesap": 1000
    }
ek_hesap_limit = 2000

def parayatır(hesap,miktar):
    if (hesap["ekHesap"]>=0 and hesap["ekHesap"]<2000):
        if miktar >=2000:
            miktar= miktar - hesap["ekHesap"]
            hesap["ekHesap"]=2000
            hesap["bakiye"] +=miktar
        else:
            hesap["ekHesap"]=2000
    else:
        hesap["bakiye"] +=miktar

def hesapBilgi(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabınız da {hesap["bakiye"]}TL bulunmaktadır, Ek hesabınız da ise {hesap["ekHesap"]}TL bulunmaktadır')
    
def paraCek(hesap,miktar):
    print(f"Hoşgeldiniz {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -=miktar
        print("Paranız veriliyor :)")
        hesapBilgi(hesap)

    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]

        if (toplam >=miktar):
            ekhesap=input(print("Paranız yetersiz Ek hesap kullanmak istermisiniz?(e/h)"))
        
            if ekhesap=="e":
                ekhesapbakiye=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"] -=ekhesapbakiye    
                print("Paranızı alabilirsiniz :)")
                hesapBilgi(hesap)
            else:
                print("Teşekkürler yine bekleriz..")
                hesapBilgi(hesap)
        else:
            print(f"Teşekkürler {hesap['hesapNo']} nolu hesabınızda bakiye yetersizdir")

parayatır(cengiz,2500)
hesapBilgi(cengiz)
# miktar=int(input("Çekilecek Tutarı Giriniz: "))
# paraCek(cengiz,miktar)

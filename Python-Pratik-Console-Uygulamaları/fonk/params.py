def toplama(a,b):
    return a+b 
def cıkarma(a,b):
    return a-b 
def carpma(a,b):
    return a*b 
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="Toplam":
        print(f1(2,5))
    elif islem_adi=="cıkarma":
        print(f2(8,7))
    elif islem_adi=="carpma":
        print(f3(2,9))
    elif islem_adi=="bolme":
        print(f4(8,4))
    else:
        print("Geçersiz İşlem")

islem(toplama,cıkarma,carpma,bolme,"Toplam")
islem(toplama,cıkarma,carpma,bolme,"cıkarma")
islem(toplama,cıkarma,carpma,bolme,"carpma")
islem(toplama,cıkarma,carpma,bolme,"bolme")

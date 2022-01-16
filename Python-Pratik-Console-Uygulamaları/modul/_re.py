import re 
# Arama modülü
str ="cengiz bugun nöbet tuttu, daha sonra eve eve geldi"

#re.findall --> kulllanımı

# result=re.findall("eve",str)  #aranacak kelime, aratılan yer
# print(result)
# result=print(len(result))

# result=re.split(" ",str) #boşluktan itibaren böler liste olarak getirir
# print(result)
# print(len(result))

# result=re.sub(" ","-",str) #değişiklik yapar
# print(result)

#result=re.search("cengiz",str) #aranacak kelimeyi bulur(yeri karakter sayısı match objesiyle döndürür)
# result=result.span()


# result=re.findall("[a-e]",str) #karakter arası, sıralı arama
# result=re.findall("[a-z]",str)
# result=re.findall("[0-9]",str)
# result=re.findall("[^abc]",str) #abc dışındakiler arar
# result=re.findall("..",str) #nokta karakter olarak kabul edilir(ikili olan herşeyi getirir)
# result=re.findall("^c",str) #a ile başlıyormu diye arar
# result=re.findall("geldi$",str) # geldi ile bitiyormu
# result=re.findall("a|b",str) #karakter içersinde ikisinden biri varmı diye kontrol eder
# result=re.findall("(a|b|c)xz",str) #gruplama yapar

print(result)
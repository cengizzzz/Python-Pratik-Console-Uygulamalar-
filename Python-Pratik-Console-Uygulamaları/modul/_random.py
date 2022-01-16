from math import floor
import random

# result=dir(random)
# result=help(random)

result=random.random() 
result=random.random() *10
result=random.uniform(0,100)
result=random.randint(1,1000)

names=["cengiz","caner","ayse","nurus","gülsever","hüseyin"]
result=names[random.randint(0,len(names)-1)]
print(result)
liste=list(range(10)) #rastgele 10 karakterli dizi oluşturur
random.shuffle(liste) #listeyi kaıştırır
result=random.sample(liste,5) #liste içersinden 5 rastgele seçer
print(result)
# OS modülü işletim sistemleri işlemleri için kullanılır
import os

#result=dir(os)
#result=os.name

#Etkin dizini ögrenme
#result=os.getcwd()

#dizin değiştirme
#os.chdir("C:\\")
#os.chdir("../..")

# yeni klasör oluşturur
#os.mkdir("yeniklasor")
#os.makedirs("yeniklasor/yeniklasorr") #klasör içinde oluşturma

#Listeleme
#result=os.listdir()
#result=os.listdir("C:\\")

#filteri dosyaları yazdırma
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

import datetime
#result=os.stat("date.py")
#result=result.st_size/1024
# result=datetime.datetime.fromtimestamp(result.st_ctime) #oluşturma tarihi 
# result=datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
# result=datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi

#os.rename("yeniklasor","yeni")
#os.rmdir("yenir") #alt dizin yoksa siler
#os.removedirs("yeni/yeniklasorr") #alt dizin varsa da siler

#os.system("notepad.exe") #sistem üzerinden program çalıştırma
#print(result)

#result=os.path.abspath("_os.py") #dosya konumunu ögrenme
#result=os.path.dirname(os.path.abspath("_os.py")) #dosya dizinini öğrenme
#result=os.path.exists("C:/Users/cengiz/Desktop/python_temelleri/_os.pyt") #dosya dizini aratma 
#result=os.path.isdir("C:/Users/cengiz/Desktop/python_temelleri/_os.py") #klasor olup olmadgını sorgular
#result=os.path.isfile("C:/Users/cengiz/Desktop/python_temelleri/_os.py") #dosya olup olmadıgını sorgular
#result=os.path.splitext("C:/Users/cengiz/Desktop/python_temelleri/_os.pyt") #dosya veya klasorün isim ve uzantısın liste olarak ayırır
print(result)
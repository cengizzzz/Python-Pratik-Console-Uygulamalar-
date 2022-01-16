# try:
#     file=open("newfile.txt","r")
# except Exception:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

from typing import ContextManager


file=open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i, end="")

#*******************read() fonksiyonu ile okuma

# content=file.read()
# print(content)

# content=file.read(10)
# content=file.read(5)
# print(content)

# Content=file.readline()
# print(Content,end="") # satır satır okuma


#************ readlines() fonksiyonu dizi şeklinde okur teker teker erişebiliriz

liste=file.readlines()
print(liste[2],end="")
file.close()
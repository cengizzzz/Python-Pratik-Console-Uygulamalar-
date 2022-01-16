# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("naberrr")

#Sayfa başında güncelleme

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     sonuc=file.read()
#     print(sonuc)

#Sayfa sonunda güncelleme(Ekleme)

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nnur atila")

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"Nur atila \n")
    file.seek(0)
    file.writelines(list)
with open("newfile.txt","r",encoding="utf-8")as file:
    print(file.read())
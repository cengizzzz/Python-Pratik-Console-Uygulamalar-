with open("newfile.txt","r",encoding="utf-8") as file: # close u direk kapatır
    content=file.read()
    print(content)
    file.seek(20) #okumadan sonra kursorun yerini belirler
    content2=file.read()
    print(content2)
    print(file.tell()) # kursor konumunu verir
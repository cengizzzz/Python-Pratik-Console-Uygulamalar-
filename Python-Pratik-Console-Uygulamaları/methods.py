class Person:
    #class attributes (sürekli kullanmayacagımız bilgiler)
    adress="keşan"

    #constructor (yapıcı metod, sürekli çalışacak olanlar)
    def __init__(self,name,year) -> None:
        self.name=name
        self.year=year
    #instance methods
    def intro(self):
        print("Merhaba, Ben "+ self.name)
    def calculater(self):
        return 2021-self.year

#object
p1=Person(name="cengiz",year=1995)
p2=Person(name="ahmet",year=1995)
p1.intro()
p2.intro()
print(f"Merhaba Adım {p1.name},Yaşım {p1.calculater()}")
print(f"Merhaba Adım {p2.name}, Yaşım {p2.calculater()}")
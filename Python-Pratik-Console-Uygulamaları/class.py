class Person:
    adress="keşan"
    def __init__(self,name,year) -> None:
        self.name=name
        self.year=year


p1=Person(name="cengiz",year=1995)
p2=Person(name="ahmet",year=1995)

print(f"p1 : Name {p1.name} Year {p1.year} Adres {p1.adress}")
print(f"p2 : Name {p2.name} Year {p2.year} Adres {p2.adress}")

print(type(Person))

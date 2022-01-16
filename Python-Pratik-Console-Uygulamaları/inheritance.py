#Inheritance (Kalıtım): Miras alma ,(Sınıf yazılan sınıftan benzerlikler alır)

#Person => name, lastname, age, eat(), run(), drink()
#Studet(Person), Teacher(Person)

class Person():
    def __init__(self,fname,lname) -> None:
        print("Person Created")
        self.fname=fname
        self.lname=lname
    def who_I_am(self):
        print("I am a person")
    def eat(self):
        print("I am eat")

class Student(Person):
    def __init__(self,fname,lname,number) -> None:
        Person.__init__(self,fname,lname)
        self.number=number
        print("Student Created")

class Teacher(Person):
    def __init__(self, fname, lname,branch) -> None:
        Person.__init__(self,lname,fname)
        self.branch=branch
    def who_I_am(self):
        print(f"I am a {self.branch} Teacher")

o1=Person("cengiz","ahmet")
o2=Student("kamil","mehmet",1340)
o3=Teacher("Hüseyin","Atila","Edebiyat")

print(o1.fname + " " + o1.lname)
print(o2.fname + " " + o2.lname + " " + str(o2.number))
o1.who_I_am()
o2.who_I_am()
o1.eat()
o2.eat()
o3.who_I_am()

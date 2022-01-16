import json

class User:
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email
    
class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedin=False
        self.currentuser={}

    def register(self, user: User):
        self.users.append(user)
        self.savetofile()
        print("Kullanıcı oluşturuldu.")
    def login(self):
        pass
    def savetofile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json","w") as file:
            json.dump(list, file)



repository=UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim=input("1- Register\n2- Login\n3 -Logout\n4- identity\n5- Exit\nSeçiminiz :")
    if  secim=="1":
        username = input("Username :")
        password = input("Password :")
        email = input("Email :")
        User=User(username=username,
        password=password,
        email=email
        )
        repository.register(User)
        print(repository.users)
    elif secim=="2":
        pass
    elif secim=="3":
        pass
    elif secim=="4":
        pass
    elif secim=="5":
        break
    else:
        print("Yanlış Seçim!")
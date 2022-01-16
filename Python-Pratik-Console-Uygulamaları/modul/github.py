import requests
from requests.models import Response

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
    
    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    def getRepositores(self,username):
        response=requests.get(self.api_url+'/users/'+username+'repos')
        return response.json

github=Github()
while True:
    print("\n")
    secim=input("1-Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçiminiz: ")
    if secim=="4":
        break
    else:
        if secim=='1':
            username=input("Username Giriniz:")
            result=github.getUser(username)
            print(f'Name: {result["name"]}\nPublic Repos: {result["public_repos"]}\nFollowers: {result["followers"]}')

        elif secim=="2":
            username=input("Username Giriniz:")
            result=github.getRepositores(username)
            
            print(result["name"])
        elif secim=="3":
            pass
        else:
            print("Hatalı Seçim Yaptınız!")
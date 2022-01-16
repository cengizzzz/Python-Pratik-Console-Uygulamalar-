import json

person='{"name":"cengiz", "languages":["python","java"]}' #cümle olarak alırsank dizini
# result=json.loads(person) #json yardımı ile dict(uyumlu dizin)'e ceviriyoruz
# #result=result["name"]
# result=result["languages"]

with open("person.json") as f:
    data=json.load(f) #json dosyasından veri çekilip yazdırılır
    print(data["name"])
    print(data["languages"])

person_dict={
    "name":"cengiz",
    "languages":"java"
}
result=json.dumps(person_dict) #json verisine dönüştürme

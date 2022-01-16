#key - value

# sehirler=["kocaeli","istanbul"]
# plakalar=[41,34]
# print(plakalar[sehirler.index("istanbul")])


# plakalar={"kocaeli":41,"istanbul":34}
# print(plakalar["istanbul"])

# plakalar["tokat"]=60

users={
    "cengizatila":{
        "age":26,
        "roles":"user",
        "mail": "c.atila60@gmail.com",
        "dogumtarih":"02.09.1995",
        "tel":"02589632124"
            },
    "caneratila":{
        "age":23,
        "roles":["admin","user"],
        "mail": "atila60@gmail.com",
        "dogumtarih":"02.09.1997",
        "tel":"02589632124"
    }
}
print(users["cengizatila"]["age"])
print(users["cengizatila"]["mail"])
print(users["cengizatila"]["dogumtarih"])
print(users["cengizatila"]["tel"])
print(users["caneratila"]["roles"][1])

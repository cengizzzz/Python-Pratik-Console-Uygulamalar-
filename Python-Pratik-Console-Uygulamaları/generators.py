# def cube():
#     for i in range(500):
#         yield i *2  #bellekte yer tutmayan deger üretir

# iterator=cube()
# for i in iterator:
#     print("İterator : ",i)

liste=(i**3 for i in range(5))
print(liste)

while True:
    try:
        generator=next(liste)
        print(generator)
    except Exception:
        break
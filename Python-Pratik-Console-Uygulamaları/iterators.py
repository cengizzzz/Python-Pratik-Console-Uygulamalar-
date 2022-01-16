
liste=[1,2,3,4,5]
iterator=iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        print(next(iterator))
    except Exception:
        break
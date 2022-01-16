#------------ENCAPSULATİON-------------

# def outer(num1):
#     print("outer")
#     def inner(num1):
#         print("inner")
#         return num1+1
#     num2=inner(num1)
#     print(num1,"\n",num2)

# outer(10)

def factorial(num):
    if not isinstance(num,int):
        raise TypeError("Sayı olması gerekiyor!")
    elif not num>=0:
        raise Exception("Pozitif sayı olması gerekiyor!")
    def inner(num):
        if num<=1:
            return 1
        return num*inner(num-1)
    return inner(num)

try:
    print(factorial(-4))
except Exception as ex:
    print(ex)

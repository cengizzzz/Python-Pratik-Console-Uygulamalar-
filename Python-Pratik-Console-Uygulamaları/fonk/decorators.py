import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("islem "+ str(finish-start) +"saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,5)
faktoriyel(6)
class circle:
    pi=3.14

    def __init__(self,yaricap) -> None:
        self.yaricap=yaricap
    
    def cevre_hesap(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesap(self):
        return self.pi* (self.yaricap** 2)

yaricap=int(input("Yarıçap değerini giriniz : "))
sec=int(input("Alan için : 1 , Çevre için : 2 değerini giriniz:  "))

hesap=circle(yaricap)

if sec == 1:
   print(f"Alan değeri: {hesap.alan_hesap()}")
else:
    print(f"Çevre değeri: {hesap.cevre_hesap()}")

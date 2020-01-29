class Car():
    def __init__(self,color,modelname,price):
        self.color = color
        self.modelname = modelname
        self.price = price
    def price_inc(self):
        self.price=(self.price*2)


merc = Car('red','abc',3534)
#bmw = Car()

merc.price_inc()
print(merc.price)
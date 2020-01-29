class Car():
    def __init__(self,color,modelname,price):
        self.color = color
        self.modelname = modelname
        self.price = price
    def price_inc(self):
        self.price=(self.price*2)


class SuperCar(Car):
     def __init__(self,color,modelname,price,cc):
         super.__init__(color,modelname,price)
         self.cc = cc

tata = SuperCar('Black',2019,757878,1100)
bmw = Car('Black',2019,757878)

print(tata.color)
print(help(tata))
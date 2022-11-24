#Static Method
class ObjectCounter:
    numberOfObjects=0
    def __init__(self):
        ObjectCounter.numberOfObjects+=1
    @staticmethod
    def display():
        print(ObjectCounter.numberOfObjects)
o1=ObjectCounter()
o2=ObjectCounter()
obj=ObjectCounter()
ObjectCounter.display()

#Inner_class
class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    def car(self):
        print(self.make,self.year)
    class Engine:
        def __init__(self,number):
            self.number=number
        def disply(self):
            print("Engine number is:",self.number)
    class Vehcile:
        def __init__(self,colour):
            self.colour=colour
        def clr(self):
            print("Colour is:",self.colour)

c=Car('BMW',2000)
print(c.make)
print(c.year)
c.car()
e=c.Engine(123)
c1=c.Vehcile("Black")
e.disply()
c1.clr()




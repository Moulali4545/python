class Car:
    manfacturer="Volkswagen"
    Gear="automatic"
    def __init__(self,name,model,cost):
        self.name=name
        self.model=model
        self.cost=cost
    def details(self):
        print(self.name,self.model,self.cost)
    @classmethod
    def man(hell):
        return hell.manfacturer
    @staticmethod
    def gear():
        return Car.Gear
c1=Car('Rolls Royce','Fantom',20000000)
print(c1.name)
print(c1.model)
print(c1.cost)
c1.details()
print(c1.man())
print(c1.gear())


# Instance method
class Mobile:
    def __init__(self,brand,cost):
        self.brand=brand
        self.cost=cost
    def details(self):
        print(self.brand)
        print(self.cost)

m1=Mobile("Iphone",125000)
m1.details()

#class method
class Pen:
    company="cello"
    model="ballpoint"
    ink="blue"
    # def __init__(self,company,ink,model):
    #     self.company=company
    #     self.ink=ink
    #     self.model=model
    @classmethod
    def details(se):
        print(se.company)
        print(se.ink)
        print(se.model)
p1=Pen()
print(p1.details())
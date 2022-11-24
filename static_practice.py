class School:
    name="DONBOSCO"
    location='DEHRADUN'
    def details():
        print("school name is ",School.name,"and it is located in ", School.location)
s=School
s.details()

#Class and Inner class

class Bike:
    def __init__(self,make):
        self.make=make
    class Model:
        def __init__(self,model):
            self.model=model
        def Model(self):
            print("model number is:",self.model)
b=Bike("Yamaha")
print(b.make)
m=b.Model("R15")
m.Model()

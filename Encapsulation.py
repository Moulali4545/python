class Student:
    def __init__(self):
        self.id=123
        self.name="sam"
s1=Student()
print(s1.id)
print(s1.name)
#Making data private and accessing the data
class Student:
    def __init__(self):
        self.__id=456
        self.__name="sammy"
    def display(self):
        print(self.__id)
        print(self.__name)

s2=Student()
s2.display()
#Accessing by Name Mangling syntax
class Student:
    def __init__(self):
        self.__id=789
        self.__name="sunny"
    def display(self):
        print(self.__id)
        print(self.__name)

s3=Student()
print(s3._Student__id)    #Name mangling syntax
print(s3._Student__name)   #Name mangling syntax
s3.display()

#practice
class Laptop:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display(self):
        print("Name is:",self.make)
        print("Model is:",self.model)
l1=Laptop("Lenovo","U0111E")
l1.display()

class Laptop:
    def __init__(self,make,model):
        self.__make=make
        self.__model=model
    def display(self):
        print("Name is:",self.__make)
        print("Model is:",self.__model)
l1=Laptop("Lenovo","U0111E")
l1.display()

class Laptop:
    def __init__(self,make,model):
        self.__make=make
        self.__model=model
    # def display(self):
    #     print("Name is:",self.make)
    #     print("Model is:",self.model)
l1=Laptop("Lenovo","U0111E")
print("Name is:",l1._Laptop__make)
print("Model is:",l1._Laptop__model)
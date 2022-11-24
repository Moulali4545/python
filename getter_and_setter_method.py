class Programer:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setId(self,Id):
        self.Id=Id
    def getId(self):
        return self.Id
    def setTechnologies(self,techs):
        self.technologies=techs
    def getTechnologies(self):
        print(self.technologies)
p1=Programer()
p1.setName("John")
p1.setId(123)
p1.setTechnologies(["HTML","CSS","JS"])
print(p1.getName())
print(p1.getId())
p1.getTechnologies()



class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        print(self.name)
    def setId(self,Id):
        self.Id=Id
    def getId(self):
        print(self.Id)
s1=Student()
s1.setName("John")
s1.setId("U06056")
s1.getName()
s1.getId()
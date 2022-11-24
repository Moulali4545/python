class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

ts=ThreeSeries("True",'BMW','328i',2003)
print(ts.cruiseControlEnabled)
print(ts.make)
print(ts.model)
print(ts.year)

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled
fs=FiveSeries('False','BMW','328i',2005)
print(fs.parkingAssistEnabled)
print(fs.make)
print(fs.model)
print(fs.year)


class School:
    def __init__(self,name,city):
        self.name=name
        self.city=city
class Student(School):
    def __init__(self,name,city,sname,rollno):
        School.__init__(self,name,city)
        self.sname=sname
        self.rollno=rollno
s=Student("Little Flower School","Delhi","John",13)
print("School name is:",s.name)
print("Located in:",s.city)
print("Student name is:",s.sname)
print("Roll no is:",s.rollno)
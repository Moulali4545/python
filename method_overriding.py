#Method overriding
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

    def start(self):
        print("Button Start")
    def stop(self):
        print("Button Stop")


ts=ThreeSeries("True",'BMW','328i',2003)
print(ts.cruiseControlEnabled)
print(ts.make)
print(ts.model)
print(ts.year)
ts.start()
ts.stop()


class School:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def display(self):
        print("Hi How are you ")
class Student(School):
    def __init__(self,name,city,sname,rollno):
        School.__init__(self,name,city)
        self.sname=sname
        self.rollno=rollno
    def display(self):
        print("Hello ")
s=Student("Little Flower School","Delhi","John",13)
print("School name is:",s.name)
print("Located in:",s.city)
print("Student name is:",s.sname)
print("Roll no is:",s.rollno)
s.display()

#Over coming the Method Overriding
# to print parent class methods,child class methods by using child class object

class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("starting the car")
    def stop(self):
        print("stopping the car")
class Threeseries(BMW):
    def __init__(self,cruisecontrolenabled,make,model,year):
        super().__init__(make,model,year)
        self.cruisecontrolenabled=cruisecontrolenabled
    def start(self):
        super().start()
        print("Button start")
    def stop(self):
        super().stop()
        print("Button stop")
    def display(self):
        print(self.cruisecontrolenabled)

ts=Threeseries("true","BMW","320i",2022)
print(ts.make)
print(ts.model)
print(ts.year)
ts.start()
ts.stop()
ts.display()


class Car:
    color='blue'
    def __init__(self):
        self.make='BMW'
        self.year=2000
c1=Car()
print(c1.make)
print(c1.year)
print(c1.color)
print(Car.color)
Car.color="red"
print(c1.color)
print(Car.color)
c1.color="white"
print(c1.color)
print(Car.color)
c2=Car()
print(c2.make,c2.year,c2.color)
c2.color="purple"
print(c2.make,c2.year,c2.color)
print(Car.color)

class Levelup:
    courseFee=30000
    courseDuration="6 months"
    courseName="FSD"
    def __init__(self):
        self.courseName="Fullstack"
        self.courseDuration="5 Months"
        self.courseFee=30000
l1=Levelup()
print(l1.courseName,l1.courseDuration,l1.courseFee)
print(Levelup.courseName,Levelup.courseDuration,Levelup.courseFee)
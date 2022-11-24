class Student:
    school='ABC'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        print("average is:",(self.m1+self.m2+self.m3)/3)
    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def average1():
        return Student.school
s1=Student(100,200,300)
print(s1.m1)
print(s1.m2)
print(s1.m3)
s1.average()
print(s1.info())
print(s1.average1())

class Employee:
    name="Steve"
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s1
        self.s3=s3
    def average(self):
        print('Average of salary is:',(self.s1+self.s2+self.s3)/3)
    def sum(self):
        print('Sum of  salary is:',(self.s1+self.s2+self.s3))
    @classmethod
    def ab(cl):
        return Employee.name
    @staticmethod
    def xyz():
        return Employee.name
s=Employee(12500,25000,30000)
s.average()
s.sum()
print(s.ab())
print(s.xyz())

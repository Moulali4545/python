class School:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def python(self):
        print("Python is easy")
    def HTML(self):
        print("HTML is easy")
class Student(School):
    def __init__(self,name,city,student_name,Roll_No):
        School.__init__(self,name,city)
        self.student_name=student_name
        self.Roll_No=Roll_No
s1=Student("Loutus Public School","Hyderabad","Gangadhar",13)
print("school name is",s1.name)
print("located in",s1.city)
print("student name is",s1.student_name)
print("Roll No is:",s1.Roll_No)
s1.python()
s1.HTML()
class Student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks
s1=Student("Chris Evans",101,99)
print(s1.name,s1.id,s1.marks)

s2=Student("Leonardo Dicaprio",102,95)
print(s2.name,s2.id,s2.marks)
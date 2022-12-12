import pickle,student
f=open("Student.dat",'wb')
s=student.Student(11,"Jhon",99.9)
pickle.dump(s,f)
f.close()
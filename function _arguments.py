# 1.Position argument
# 2.Default argument
# 3.Variable length argument
# 4.Keyword variable length argument

#1. position Argument:
def person(name,age):
    print(name)
    print(age)
person('Moulali',22)
person(age=45,name="Moulali")

#2.Default Argument:
def average(a=10,b=20):
    c=(a+b)/2
    print(c)
average()
average(a=22,b=23)

#3.Variable length Argument
def sum(a,b,c,d):
    c=a+b+c+d
    print(c)
sum(2,3,4,5)
print()
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
        print(c)
    print(c)
sum(1,2,3,4,5,6,7,8,9)

#4.Keyword variable length argument:
def person(name,*data):
    print(name)
    print(data)
person("moulali",30,'delhi',9100690931,'fsd')
print()
def person(name,**data):
    print(name)
    print(data)
person("moulali",age=20,city='delhi',phone=9100690931,course='FSD')
#to iterate over dictionary
print()
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person("moulali",age=20,city='delhi',phone=9100690931,course='FSD')



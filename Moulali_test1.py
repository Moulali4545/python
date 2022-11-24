# 1. question
tpl=('USA','UK','Canada')
l1=list(tpl)
print(l1)
l1.append('India')
print(l1)
l1=tuple(l1)
print(l1)
#2.question
s='Python training at levelup'
print(s[::-1])
#3.question
for i in range(1,100):
    if(i%3==0 or i%5==0):
        print(i,end=',')
#4 question
for i in range(0,20):
    if(i%2!=0):
        print(i,end=',')
print()
#5.question
a=int(input('Enter a number:'))
i=1
while(i<=10):
    print(a,"*",i ,"=",a*i)
    i=i+1

#6.question
age=25
def vote(age):
 if(age<18):
    print("Not Eligible")
 else:
    print("Eligible")

vote(age)

#7.question
def add(a,b):
    return a+b
def sub(x,y):
    return x-y
def mul(p,q):
    return p*q

#9 .question
lst=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda x:x%2!=0,lst))
print(odd)

#10.question
a=10
b=float(a)
print(b)
print(type(b))
tpl=(1,2,3,4,5,6)
s1=set(tpl)
print(s1)
print(type(s1))
x="123"
y=int(x)
print(y)
print(type(y))




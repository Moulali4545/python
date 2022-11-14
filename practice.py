#function to add 3 numbers
from cmath import pi
def add(a,b,c):
    return a+b+c
print('sum of three numbers is:',add(10,20,30))
print()
#function to find average of two numbers with return 
def avg(x,y):
    return (x+y)/2
print('Average is :',avg(10,20))    
print()
#function to find average of two numbers without return
def avg(x,y):
    avg=(x+y)/2
    print('Average is:',avg) 
avg(10,20)
print()
#function to find area of circle
def area(r):
    return pi*r**2
area=area(5)
print("Area of circle is:",area)
print()
#function to change first three elements of a list
def change(l1):
    l1[0]=10
    l1[1]=20
    l1[2]=30
    print("After changing elements:",l1)
l1=[1,2,3,4,5]
change(l1)
print()
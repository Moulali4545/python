#average of two numbers
def avg(x,y):
    z=(x+y)/2
    print(z)
avg(20,21)
# Numbers ftom 1 to 25 excluding multiples of 3
for i in range(1,26):
    if i%3==0:
        continue
    else:
        print(i,end=" ")

#multiplication of two numbers
print()
def mul(a,b):
    c=(a*b)
    print(c)
mul(10,11)
print()
#Function to return avg of two nummbers
def avg(a,b):
    return (a+b)/2
# print(avg(10,12))
result=avg(10,12)
print(result)
#function to return multiple values
def calc(x,y):
    a=x+y
    s=x-y
    m=x*y
    d=x/y
    return a,s,m,d
print(calc(10,2))
#iterate the values of tuple
result=calc(10,2)
for i in result:
    print(i)

#change elments in list
def update(lst):
    lst[3]=20
    print('list is:',lst)
lst=[10,20,30,40]
update(lst)    
#change element in tuple
def update(tpl):
    x=list(tpl)
    x[3]=100
    print(x)
    y=tuple(x)
    print(y)
tpl=(10,20,30,40,50)
update(tpl)

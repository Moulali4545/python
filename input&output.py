#Input function
s=input('Enter your name:')
print(s)
#Reading charadter
ch=input('Enter your name:')
print(ch[3])
#reading expression
result=eval(input('Enter an expression:'))
print(result)
#read multiple inputs
lst=[int(x) for x in input("enter multiple values:").split()]
print(lst)
lst=[float(x) for x in input("enter multiple values:").split()]
print(lst)
lst=[str(x) for x in input("enter multiple names:").split()]
print(lst)
x,y,z,w=[int(x) for x in input("enter two values").split()]
print('First number is:',x)
print('second number is:',y)
#User input using map method
c=list(map(int,input("enter multiple values:").split()))
print(c)
c=list(map(float,input("enter multiple values:").split()))
print(c)
c=list(map(str,input("enter multiple Names:").split()))
print(c)


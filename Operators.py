#1.Arithmetic_operators 
# +,-,*,/,//,%,**

a=10
b=5
print("Addition is:",a+b)
print("subtraction is:",a-b)
print("Multiplication is:",a*b)
print("Division is:",a/b)
print("floor div is:",a//b)
print("power is:",a**b)
print("modulus:",a%b)
#2. Assignment operator - "="
a=10
b=2
print(a,b)

#3.compound arithmetic operators 
a += b
print(a)     #a=a+b
a -= b
print(a)      #a=a-b
a *= b
print(a)      #a=a*b
a /= b
print(a)     # a=a/b
a **=b
print(a)     #a=a**b
a %= b
print(a)     #a=a%b
#4.Comparison Operator
x=50
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
#5.Identity Operators
print()
x=[1,2,3]
y=[1,2,3]
y=x
print(x==y)
print(x is y)
z=x
print(z is x)
print(z is not x)
print()
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
#6.Logical operators 
# are used to combine conditional statements
#'and','or' and 'not
print()
x=20
y=30
print(x==20 and y==31)
print(x==20 and y==30)
print(x>=25 or y==31)
print(x<25 or y==31)
print(not(x==20 and y!=30))
print()
#7.Membership operators 
# are used to test if an element is present in sequence or not
#'in' and 'not in'

lst=['hi','helo','bye',"bye"]
print('helo' not in lst)
print('bye' in lst)
print("hi in lst")
print("hello" in lst)






#write a python program that accept 3 numbers from user and calculate average
a,b,c=[int(x) for x in input("enter three numbers:").split(",")]
result=(a+b+c)/3
print("average is",result)

tpl=(1,2,3,4,5,6,7,8)
def greet(name ):
    return "hello"+name
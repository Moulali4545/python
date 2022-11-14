#1.Global variable
#2.Local variable


x=2022   #global
def display():
    y=2021      #local
    print(y)
    print(x)
print(x)
display()

#Accessing glabal,local variables with same name;
a="Moulali"
def display():
    a="Rohit Sharma"
    print(a)
    print(globals()['a'])
print(a)
display()

#Function passed parameter to another function:
print()
def display(fun):
    return "Hi" + fun
def name():
    return "Moulali"
def show():
    return " Virat"
print(display(show()))



print()
#Assigning function to variable
a=13
def display():
    a=12
    print(a)
    print(globals()['a'])
print(a)
b=display    #Assigning function
b()

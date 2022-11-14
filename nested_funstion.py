def outer_function(fun):
    def inner_function():
        return "Hi"+fun
    return inner_function()
print(outer_function(" John"))
print()
def display(fun):
    def message():
        return "Hi," +fun
    return message()
print(display("How are you"))


#Pass sequence types to functon :
#we can pass sequence types like list's,tuple's,set's etc...
def myfun(lst):
    for i in lst:
        print(i,end=" ")
myfun([1,2,3,4,5,6,7])


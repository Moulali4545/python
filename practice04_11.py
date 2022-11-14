#retrive numbers divisible by 5 in lst
def result(lst):
    for i in lst:
        if i%5==0:
            print(i,end=" ")
result([1,2,3,4,5,6,10,12,15,20,44,45,25,50]) 
print()           
#map 4 to each elements of list
lst=[1,2,3,4,5]
result=list(map(lambda a:a+4,lst))
print(result)
#reduce list=[1,2,3,4] to single value by finding the product
from functools import reduce
lst=[1,2,3,4]
a=reduce(lambda x,y:x*y,lst)
print(a)
#nested function
def outer_function(fun):
    def inner_function():
        return  'Good'+fun
    return inner_function()
print(outer_function(' Morning'))        
#passinfg any type to functiontuple and point only odd numbers
tpl=(1,3,4,5,6,7,8,9,10,11,12,13,14,15)
result=tuple(filter(lambda x:x%2!=0,tpl))
print(result)
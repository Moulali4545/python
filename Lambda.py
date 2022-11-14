# Lambda functions
#   Are small anonymous functions that will not have any name

# Syntax
# lambda argument_list:expression
# lambda functions can have multiple arguments but only one argument

def result(x):
    return x*x
print(result(3))

print()
f=lambda x:x+x
print(f(3))

# #Lambda methods
# 1.filter()
#     filter out sequence of elements depending on some logic and condition
lst=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2==0,lst))
print(result)

# 2.map()
# maps out sequence of elememts depending on some logic and condition
lst=[1,2,3,4,5,6,7,8]
result=list(map(lambda x:x*2,lst))
print(result)

# #3.Reduce()
# Reduce the sequence of elements into single value depending on some logic and sequence
from functools import reduce
lst=[5,10,15,20]
result=reduce(lambda x,y:x+y,lst)
print(result)
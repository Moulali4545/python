#create a tuple
from audioop import reverse
tpl=(10,)
print(tpl)
print(type(tpl))
#indexing()
tpl=(10,20,30,40,50)
print(tpl[1])
print(tpl[0])
#slicing()
tpl=(10,20,30,40,50)
print(tpl[0:])
print(tpl[:3])
#adding elements into tuple
t=('Audi','BMW')
t1=list(t)
t1.append('Mercedes')
print(t1)
#nested tuple
tpl=('hello','hi',(1,2,3),('xyz'))
print(tpl[0])
print(tpl[3])
print(tpl[0])
print(tpl[1])
#memership operators
tpl=(10,20,30,40,50)
print(10 in tpl)
print(15 in tpl)
print(100 not in tpl)
#tuple concatination
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)
print((1,2,3)+t2)
#tuple constructor
mytpl=tuple(('BMW','Audi','Ferari'))
print(mytpl)
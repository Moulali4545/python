#creating a set
s={10,20,30,'xyz',10,20}
print(s)
print(type(s))
#add items to the set
s.add(30)
print(s)
#remove items from the set
s.remove(30)
print(s)
#find length of the set
print(len(s))
#convert a set into frozen set
s={1,2,3}
print(s)
print(type(s))
#covert
f=frozenset(s)
print(f)
print(type(f))
#set methods- coppy(), difference()
#copy()
s1={1,2,3}
print(s)
s2=s1.copy()
print(s2)
s2=set(s1)
print(s2)
#difference()
x={'hello','hi','good'}
y={'hello','polite','morning'}
z=x.difference(y)
print(z)
#find common elements from sets
s={1,2,3,'1'}
t={1,'1',5}
z=t.intersection(s)
print(z)
#set constructor
myset=set(('hi','hello','Good morning'))
print(myset)
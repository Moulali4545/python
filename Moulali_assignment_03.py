#create a list
lst=[1,2,3]
print(lst)
#find the length of list
print(len(lst))
#add elements to list
lst.append(10)
print(lst)
#remove elements in thelist
lst.remove(3)
print(lst)
#indexing()
lst1=[1,2,3,4,56]
print(lst1[2])
print(lst1[1])
#slicing()
lst2=[10,20,40,20,50,'java',-11,-30,30.4]
print(lst2[0:4])
print(lst2[:3])
#joining two lists
lst1=[1,2,3,4,56]
lst2=[10,20,40,20,50,'java',-11,-30,30.4]
d=lst1+lst2
print(d)
print([1,2,3,4,56]+lst2)
print(lst1+lst2)
#list methods
#extend()
lst1=[1,2,3,4,56]
lst1.extend([10,20,30])
print(lst1)
#insert()
lst1.insert(2,100)
print(lst1)
#remove()
lst1.remove(100)
print(lst1)
#max(),min()
print(max(lst1))#56
print(min(lst1))#1
#sort()
lst1.sort() # ascending order
print(lst1)
lst1.sort(reverse=True)
print(lst1)#descending order
#pop()
lst1.pop(2)
print(lst1)
#copy()
l1=[1,2,3]
l2=l1.copy()
print(l2)
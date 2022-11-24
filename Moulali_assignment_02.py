#create string
a='hi'
print(a)
print(type(a))
#assign string to a variable
s='python is easy'
print(s)
#indexing
s='python is easy'
print(s[0])
print(s[5])
print(s[-2])
# slicing
print(s[0:6])
print(s[:9])
print(s[:-2])
print(s[:14])
#step value to slice
print(s[0:9])
print(s[0:9:2])# it will skips the multiples of 2
print(s[0:14:3])
print(s[::-1])# it will display the reverse formate
print(s[:9])
print(s[0:])
#string methods
#strip()
s=' you are Beautiful '
print(s)
print(len(s))
print(s.strip())# it will remove the white spaces
print(s.lstrip())#it will comes left side
print(s.rstrip())#it will comes right
#find() -locate a substring in given string
print(s.find('e'))
print(s.find('a'))
#count()-return the number of occurences specific elements
print(s.count('a'))
print(s.count('e'))
#replace
print(s.replace('Awesome','cool'))
print(s)
# upper(),title(),lower()
print(s.upper())
print(s.lower())
print(s.title())
#split()=splits the substrings if it finds instances of separtors
a='Hello,World'
print(a)
print(a. split(','))
b='he lloworld'
print(b. split(','))
#s='12344'
s='you are awesome'
print(s. isdigit())
print(s.startswith('y'))
print(s.endswith(''))
print(s.swapcase())
#check string -'in' and 'not in'
txt=' no gain with pain'
print('ain' in txt)
print('out in txt')
print("out" not in txt)
#string concatination-jining /combining
a='Hello'
b='World'
print(a+b)
print(a+' ' +b)
c=a+ ' '+b
print(c)
#length of string
print(len(s))
x='hello'+'100'
print(x)
#
mystr='levelup'
print(mystr)
print(len(mystr))
s1='levelup'
print(s1*3)
print((s1+" ")*3)
# using .format method
age=10
marks=99
txt='my nmae is john and Iam {},marks are{}'
print(txt.format(age,marks))
# string are immutable
print('hi')
print('hi')
print('hi')
print('hi')
print('hi')
print('hi')
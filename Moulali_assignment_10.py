#print numbers 20 19 18 17 16 15
i=20
while(i>14):
    print(i,end=" ")
    i-=1
# from 20 to 30 print numbers till 25
print()
for i in range(20,30):
    if i==26:
        break
    print(i,end=" ")
# in string levelp print level
print()
x='Levelup'
for i in x:
    if i=='u':
       break
    print(i,end=" ")    
#copy file
f=open("flower.jpg",'rb')
f1=open("India 2.jpg",'wb')
for i in f:
    f1.write(i)

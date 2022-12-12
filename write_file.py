# f=open("myfile.txt","w")
# s=input("Enter text:")
# f.write(s)
# f.close()

f=open('myfile.txt','w')
print("Enter the text,type # when you are done")
s=" "
while s!="#":
    s=input()
    f.write('\n')
    f.write(s)
f.close()
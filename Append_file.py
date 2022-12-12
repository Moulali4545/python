#Append file=current content will not be deleted
f=open("myfile.txt","a")
s=input("Enter text:")
f.write(s)
f.close()
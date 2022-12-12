import os,sys
if os.path.isfile("myfile.txt"):
    f=open('myfile.txt','r')
    s=f.read()
    print(s)
    f.close()
else:
    print("file does not exist")
    sys.exit()

check_file=os.path.isfile("myfile.txt")
print(check_file)
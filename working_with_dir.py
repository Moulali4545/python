import os
print(os.getcwd())
print(os.listdir())
#Creating a directory
# os.mkdir("My Pics")
# print(os.listdir())
#Rename a directory
# os.rename("My Pics","My Images")
# print(os.listdir())
#Deleting a directory
# os.rmdir("My Images")
# print(os.listdir())
#Check Directory
print(os.getcwd())
check_dir=os.path.isdir('C:\\Users\Admin\Desktop\\fullstack')
print(check_dir)
#Program to check the file is Exist or not.
import os
if os.path.exists("data1.txt"):
    print("File is exist")
else:
    print("File is not exist")
#Program to Read text from File. (File Must be created before reading) at default location.
file=open("data.txt",'r')
content=file.read()
#Write a program to save the output of program in a file
print(content)
file.close()

#Create a file By using w mode
f=open("data1.txt","w")
f.write(content)
f.close()

#Create a Program to Writing in file using writelines function.
file1 = open("data1.txt", "w")
lst = []
for i in range(3):
    name = input("Enter the name of the employee: ")
    lst.append(name + '\n')

file1.writelines(lst)
file1.close()
print(lst)
print("Data is written into the file.")
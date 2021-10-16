import os

class File:
    def  __init__(self,path):
        self.path = path

    def create(self):
        print("---------The file is being prepared to write--------")
        print()
        message = input("Type the content for the file : ")
        with open(self.path,'w') as f:
            f.write(message)
            f.close()
        print()
        print("Your file is successfully created and the content is written ")
        print("##############################################################")

    def read(self):
        print("---------The content of the file is being read--------")
        print()
        try:
            with open(self.path,'r') as f:
                x=f.readline()
                print(x)
        except (FileNotFoundError):
            print("There is no file exist named"+self.path.split('/')[-1])

    def delete(self):
        try:
            print("The file is being prepared to delete from the disk")
            os.remove(self.path)
            print("Your file is Deleted succesfully")
        except(FileNotFoundError):
            print("There is no file exist named" + self.path.split('/')[-1])

    def append(self):
        try:
            with open(self.path,'a+') as f:
                l=[]
                try:
                    n = int(input("Enter the number of lines to you want to append : "))
                except(ValueError):
                    print("The path file must be a string [ eg : D:/folder/folder2/file.any_extension ]")
                    exit()
                l= [input() for i in range(n) ]
                for i in l:
                    f.writelines(i+"\n")
                f.close()
        except(FileNotFoundError):
            print("There is no file exist named"+self.path.split('/')[-1])


print("##########  Program to create , read , and Delete files ############")
print("The following below actions can be done ")
print("\n1)Create a new file and write the content\n2)Read the content of the existing file\n3)Delete a file\n4)Write content to the existing file \n")
print("Enter the option you want to proceed with :")

try:
    option = int(input())
except(ValueError):
    print("The path file must be a string [ eg : D:/folder/folder2/file.any_extension ]")
    exit()

path = input("Enter the path for the file suitable for the above listed actions : ")
#print("The path file must be a string [ eg : D:/folder/folder2/file.any_extension ]")
o = File(path)
if(option == 1):
    o.create()
elif(option == 2):
    o.read()
elif(option == 3):
    o.delete()
elif(option == 4):
    o.append()
else:
    print(" Invalid option [ Enter any option from 1 to 4 ]")

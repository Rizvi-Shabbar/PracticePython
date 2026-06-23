# Program based on walrus operator, list merge, type definations and exception handling

# 1. write a program to open 3 files file1.txt,file2.txt,file3.txt if any these files are not present
# a msg without existing the program must be printed prompted the same
try:
    with open("file1.txt","r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("file2.txt","r") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("file3.txt","r") as f3:
        print(f3.read())
except Exception as e:
    print(e)

print("Done!")

# 2. write a program to print 3rd,5th,7th element of a list using enumerate

l = [1,2,3,4,5,6,7]

for index,item in enumerate(l):
    if(index == 2 or index == 4 or index == 6):
        print(f"The value at {index} is {item}")

# 3.write a list comp to print a list which contain table of a num entered by a user
n = int(input("Enter the number : "))
table = [n*i for i in range(1,11)] #list comp
print(table)

# 4. store table from problem 3 into table.txt file

n = int(input("Enter the number : "))
table = [n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n} : {str(table)} \n")
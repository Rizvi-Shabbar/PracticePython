# Program based on lambda func,join method,virtual env,map

# 1.write a program to take name,marks and phone no as a input and print result with the help of format .
name = input("Enter the name : ")
marks = int(input("Enter the marks : "))
phoneNo = int(input("Enter the phone number : "))

s = "The name of student is {} and his marks is {} and his phone number is {}".format(name,marks,phoneNo)

print(s)

# 2. A list contain multiplication table of 7. write a program to convert it to vertical strings of a
# same number
table = [str(7*i) for i in range(1,11)]
print(table)
s = "\n".join(table)
print(s)

# 3.write a program to filter a number in a list divisible by 5

a = [5,10,234,433,876,555,1000,1560]

def divBy5(n):
    if(n%5==0):
        return True
    return False

result = filter(divBy5,a)
print(list(result))

# 4.write a program to find greater of a num in a list using reduce method
from functools import reduce

a1 = [1,2,3,999,43553,32,76,9876,100000000]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a1))


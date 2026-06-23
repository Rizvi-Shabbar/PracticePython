# Programs based on loops

# 1.python program to print table of a given number using for loop

n = int(input("Enter the number :"))

for i in range(1,11):
    print(f"{n} * {i} == {n*i}")



# 2.python program to greet a person in a list whose name starts with s

l = ["Rizvi","Rasulpur","Shabbar","Rohan","Ritik","Shashank"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")
    
# 3. program 1 with while loop
n = int(input("Enter the number : "))
i=1
while(i<11):
    print(f"{n} * {i} == {n*i}")
    i+=1

# 4.find a given number is prime or not

n = int(input("Enter the number : "))
for i in range(2,n):
    if (n%i)==0:
        print("Number is not a prime ")
        break
else:
    print("Yes No is Prime")

# 5.Sum of first n natural number using while loop

n = int(input("Enter the number : "))

sum = 0
i=1
while(i<n+1):
    sum+=i
    i+=1
print("Sum of the number : ",sum)

# 6.python program to find the factorial of a given number using for loop
n=int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(f"factorial of {n} is : {fact} ")

# 7.print the following star pattern
#    *
#   ***
#  ***** for n=3

n = int(input("Enter the number : "))
for i in range(n+1):
    print(" "*(n-i),end="") # for star pattern first print space and then star
    print("*"*(2*i-1),end="")
    print("")

# 8.Python program to print a table of a given no in reversed order

n = int(input("Enter the number : "))
for i in range(1,11):
    print(f"{n}*{11-i} == {n*(11-i)}")





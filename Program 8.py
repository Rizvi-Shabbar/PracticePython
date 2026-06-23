# Tuples and list program


# 1.Store seven fruits in a list entered by the user
fruits = []
f1 = input("Enter the fruit : ")
fruits.append(f1)
f2 = input("Enter the fruit : ")
fruits.append(f2)
f3 = input("Enter the fruit : ")
fruits.append(f3)
f4 = input("Enter the fruit : ")
fruits.append(f4)
f5 = input("Enter the fruit : ")
fruits.append(f5)
f6 = input("Enter the fruit : ")
fruits.append(f6)
f7 = input("Enter the fruit : ")
fruits.append(f7)

print(fruits)

# 2.write a program to accept marks of 3 students and placed them in a sorted order
marks = []
m1 = int(input("Enter the marks : "))
marks.append(m1)
m2 = int(input("Enter the marks : "))
marks.append(m2)
m3 = int(input("Enter the marks : "))
marks.append(m3)

print(marks)
marks.sort()
print(marks)

# 3. sum a list of 4 number
l1 = [1,3,4,8]
print(sum(l1))

# 4. write a program to count zero in the following tuple

t = (7,0,8,0,0,9)
cnt = t.count(0)
print(cnt) # retunr 3
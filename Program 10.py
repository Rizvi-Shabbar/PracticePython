# Programs base on conditions
# 1.write a python program to taka marks as a input of 3 subjects and student will pass
# if he secure overall 40% marks and 33% in all the 3 subjects.

marks1 = int(input("Enter the marks of Hindi : "))
marks2 = int(input("Enter the marks of english : "))
marks3 = int(input("Enter the marks of Maths : "))

total_Percentage = (marks1+marks2+marks3)/3

if(total_Percentage>=40 and (marks1>33) and (marks2>33) and(marks3>33)):
    print("Student Passed with total percentage of : ",total_Percentage)
else :
    print("Student fail and got total percentage :",total_Percentage)

# 2.write a python program to take 4 phrases as input considered as scam if in your input
# those phrases exit print scam other wise print your msg hint use (in) keyword

p1 = "want to earn money"
p2 = "gave us OTP"
p3 = "SMS"
p4 = "fraud call"

msg = input("Enter the input message :")
print("Identifying the source of msg whether its scam or not................ ")
if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This is scam")
else:
    print("This is not a scam")


# 3. write a python program whether a given name is present in a list or not

list = ["Shabbar","Rizvi","Shashank","Rahul","Abhinav"]
name = input("Enter the name :")
if(name in list):
    print("Yes name is in list")
else:
    print("Name is not in list")

# 4.write a python program to calculate the grade of a student 
marks = int(input("Enter the marks : "))

if(marks>90 and marks<=100):
    grade = "Excellent"
elif(marks>80 and marks<=90):
    grade = "A"
elif(marks>70 and marks<=80):
    grade = "B"
elif(marks>60 and marks<=70):
    grade = "C"
elif(marks>50 and marks<=60):
    grade = "D"
else:
    grade = "F"

print("The grade of student : ",grade)
# Program based on class and objects :
# 1.python program to stored a information of employee working in Microsoft

from random import randint
class Employee:
    company = "Coforge"

    def __init__(self,name,salary,EmpId):
        self.name = name
        self.salary = salary
        self.EmpId = EmpId

E1 = Employee("Shabbar",37500,130255)
print(E1.name, E1.salary, E1.EmpId,E1.company)

E2 = Employee("Shams",37500,130210)
print(E2.name, E2.salary, E2.EmpId, E2.company)


# 2.create a class calculator and find square,cube and square root of a number

class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"Square of a given number {self.num} : {self.num * self.num}")
    
    def cube(self):
        print(f"Cube of a given number {self.num} : {self.num * self.num * self.num}")
    
    def square_root(self):
        print(f"SquareRoot of a given number {self.num} : {self.num ** 1/2}")

    @staticmethod
    def greet():
        print("Hlo !!Good Afternoon")
    

obj = Calculator(8)
obj.square()
obj.cube()
obj.square_root()
obj.greet()

# 3.cretae a class attribute a and then assign that attribute 0 with the help of object directly
# does the class attribute change = ? and Answer is No

class Demo:
    a = 5 # class attribute cannot change with the help of object

A = Demo()
print(A.a) #print 5 bcoz instance attribute is not there
A.a = 0
print(A.a) # print 0 bcoz instance attribute is created and it takes prefernce over class attribute
print(Demo.a) # print 5 bcoz class attribute will not change only if instance obj is cretaed than 
# value of instance attribute print 

# 4.Add a static method in problem 2 ,to greet the user with hello
# 5.create a class train and book a ticket with ticket no and and find the status of train whether it
# is running or not and calculate fair based on destination 

class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def BookTicket(self,fro,to):
        print(f"Train No {self.trainNo} is succesfully booked from {fro} to {to}")
    
    def getStatus(self,pt_No):
        print(f"Train No {self.trainNo} is successfully coming towards sakoti at platform No {pt_No}")

    def CalFare(self,fro,to):
        print(f"Fare of the train from {fro} to {to} is : {randint(55,3255)} ")

tt  = train(245536)
tt.BookTicket("Sakoti","Delhi")
tt.getStatus(3)
tt.CalFare("Sakoti","Delhi")

# 6.if we remove self and place any random value instead of self then it will work or will give
# error ? Answer is it will work bcoz we can use any value instead of self but writing self is
# good practice for program readability


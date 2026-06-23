# Program base on functions and recursion
# 1.find greatest of 3 numbers

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print("Greatest number among a,b,c is :",greatest(10,78,-1))

# 2.convert celsius to farenhiet

def c_to_f(c):
    ft = (c*1.8)+32
    return ft

c =int(input("Enter the temperature in celsius : "))

ft = c_to_f(c)

print(f"Conversion from celsius {c} to farenhiet equals to : {ft} ")

# 3.Calculate the sum of first n natural number using recursive function

def find(n):
    if(n==1):
        return 1
    return n+find(n-1)

n = int(input("Enter the number : "))
sum = find(n)
print("Sum of the natural number is : ",sum)

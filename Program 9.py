# 1.write a python program take hindi word as a key and english word as a value in a dict then take input
#  from user which key you want to print

words = {
    "kutta" : "dog",
    "billi" : "cat",
    "madad" : "help",
    "Maa" : "mother"

}

print(words)
print(words.items())

word = input("Enter the word you want the value of : ")
print(words[word])

# 2.Take 8 num as a input and print unique no hint use set

st = set()
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))
n = input("Enter the number : ")
st.add(int(n))

print(st)

# 3.Can we have a set 18 as int or "18" as string 
s =set()
s.add(18)
s.add("18")

print(s) #hence the answer is yes

# 4. what will be the length of this below set
s1 =set()
s1.add(20)
s1.add(20.0)
s1.add("20")

print(len(s1)) #return len 2 because python compare value if they equal then it consider same or true
# thats why len is 2 not 3
print(s1)

# 5.write a python program to create empty dict and take 4 friends name as a key and favourite
#  language as a value as input and print dict

dict ={}

name = input("Enter the friends name : ")
lang = input("Enter the favourite lang : ")

dict.update({name:lang})

name = input("Enter the friends name : ")
lang = input("Enter the favourite lang : ")

dict.update({name:lang})

name = input("Enter the friends name : ")
lang = input("Enter the favourite lang : ")

dict.update({name:lang})

name = input("Enter the friends name : ")
lang = input("Enter the favourite lang : ")

dict.update({name:lang})

print(dict)

# 6. what if name of 2 friends are same (key is same)
# then it will print the last value of same friends

# 7.what if lang of 2 friends are same (value is same)
# lang can be same becoz it is value not key and value can be same but key cant


# 8.can you change the values inside a list which is contained in set(S)
s2 = {8,7,12,"Rizvi",[1,2]}

# No we cant becoz set m inexing nhi hoti
# so the answer is we cannot include list inside set
# To achieve this we can use a tuple instead of a list becoz  tuple are immutable and hashable

 
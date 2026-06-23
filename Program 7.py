#  Program 1 string replace method
name = ''' Dear <|Name|>
    You are selected
    for the Graduate Engineer Trainee Role 
    at <|Date|>
''' 

print(name)

print(name.replace("<|Name|>","Shabbar").replace("<|Date|>","15 Jan 2025"))
# repace make new string and change that string original str can't be change

#  Program 2 find double space in a string
str = "Shabbar is a  cool boy"

print(str.find("  ")) # find returns the index of whaterver you find if not exist then return -1

#  String are immutable you cannot change them by running or string functions return new string after 
#  changes

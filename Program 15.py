# programs based on inheritance
# 1. create a class with 2-d vector create another class 3-d vector and print all the 3 vectors

class TwodVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The  2d vector is : {self.i}i + {self.j}j")

class ThreedVector(TwodVector):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k  = k
    def show(self):
        print(f"The  3d vector is : {self.i}i + {self.j}j + {self.k}k")

a = TwodVector(4,7)
a.show()
b = ThreedVector(2,3,5)
b.show()

# 2.create a class pets from Animals and further dog from pets.Add a method bark to class dog

class Animals:
    pass
class pets(Animals):
    pass
class dog(pets):
    def bark(self):
        print("dogs are barking")

d = dog()
d.bark()

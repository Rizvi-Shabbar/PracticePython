# Program based on file
import random
# 1.we have a text file poem.txt find "twinkle is present inside it"

f = open("poem.txt")
data = f.read()
if("twinkle" in data):
    print("twinkle is present in a file")
else:
    print("twinkle is not present")
f.close()

# 2.write a program to generate table from 2 to 20 and place them into different 20 files
# inside a single folder

def generate_table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    generate_table(i)

# 3.The game() function in a program lets a user play a game and return score as an integer. You need 
# to read a file HiScore.txt which is either blanks or have previous hiscore You need to write a program
# to update the hiscore whenever the game function break the hiscore .

def game():
    print("You are playing the game.....")
    score = random.randint(1,99)
    with open("Hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is {score}")
    if(score > hiscore):
        with open("Hiscore.txt","w") as f:
            f.write(str(score))
        
    return score

game()
'''
1 for sanke
-1 for water
0 for gun
'''
import random


computer = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youDict = {"s": 1, "w": -1,"g":0}
reverseDict = {1: "sanke", -1: "water", 0:"gun"}
you = youDict[youstr]

print(f" you chose:{reverseDict[you]}\ncomputer choose:{reverseDict[computer]} ")

if(computer == you):
     print("its drow") 

else:     

    if(computer ==-1 and you ==1):
        print("you win")

    elif(computer ==-1 and you ==0):
        print("you lose!")

    elif(computer ==1  and you ==-1):
        print("you lose!")    

    elif(computer ==1  and you ==0):
        print("you win") 

    elif(computer ==0  and you ==-1):
        print("you win") 

    elif(computer ==0  and you ==1):
        print("you win!")  

    else:
        print("something went wrong")     


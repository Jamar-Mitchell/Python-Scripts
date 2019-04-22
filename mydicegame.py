#! /usr/bin/python
import random
import sys; print(sys.version)

playgame= "y"
result= 99
playerscore=0
compscore=0

def rolldice():
    result= random.randint(1,6)
    return result
    
while(playgame == "y"):
    print("Would you like to roll the dice? y/n")
    playgame = input()
    if(playgame == "y"):
       player= rolldice()
       comp=rolldice()
       print("Computer rolled a "+ str(comp) )
       print("Player rolled a "+ str(player) )
       if(player>comp):
           playerscore+=1
           print("Darn you won this sucks")
           
       elif(player<comp):
           compscore+=1
           print("I won ahahah chalk one up for patchy!")
            
       else:
           print("Dwow its a tie thats no fun")
       print("user:"+str(playerscore)+"  "+"computer:"+str(compscore)+"\n")    
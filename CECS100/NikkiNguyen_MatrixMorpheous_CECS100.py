'''
Student Name: Nikki Nguyen
Professor Name: Elleni Wolde
Class: CECS 100
Date: 10/28/2015
'''
from time import sleep
import sys

def main():
    userSelect = 0
    stam = 0
    dodge = 0
    menu()
    userSelect = menuSelect(userSelect)
    selection(userSelect,stam,dodge)
    
    
def menu():
    print("*********************Welcome to the Matrix Project!*********************")
    print("List of Characters:")
    print("Press 1 for Morpheus")

def menuSelect(userSelect):
    userSelect = int(input("Please select a character: "))
    return userSelect

def selection(userSelect,stam,dodge):
    if userSelect == 1:
        morpheus()
        stamina(stam)
        defense(dodge)
    if userSelect != 1:
        print("Invalid Input, only one character available!")
        userSelect = int(input("Please select a character: "))
        selection(userSelect,stam,dodge)
        
    
def morpheus():
    print()
    print("You have selected Morpheus!!!\n")
    sleep(1)
    print("****Morpheus' big battle****")
    sleep(1)
    print('***Morpheus, Trinity, Cypher, and Neo hide inside the wall behind the bathroom from the agents and police***')
    sleep(2)
    print('**Morpheus notices that Agent Smith grabbed Neo through the wall!**')
    sleep(2)
    print()
    print('-OOOOOOOOOOOOOOOHHH!!!!!!!-')
    sleep(2)
    print('Morpheus crashes through the wall onto Smith!!!!')
    sleep(2)
    print('The others escape down the wall')
    sleep(2)
    print('Smith- Ahhhh the great Morpheus, we meet at last')
    sleep(2)
    print('-And you are?-')
    sleep(1)
    print('Smith- A Smith, Agent Smith')
    sleep(1)
    print("-Ya'll look the same to me!-")
    sleep(3)
    print()
    print("***Morpheus headbutts Smith!***")
    print("(   #  õ_ó)(ó_õ  #   )")
    sleep(2)
    print("**Upset, Smith does it 3x over!!!!**")
    print("(   #  õ_ó)(ó_õ  #   )")
    print("(   #  õ_ó)(ó_õ  #   )")
    print("(   #  õ_ó)(ó_õ  #   )")
    sleep(1)
    print("**Smith lands a jab and Morpheus hurdles into the wall**")
    print("(/ .□.)\ ︵╰(゜益゜)")
    sleep(2)
    print()
    print("--Morpheus gets up and fights Smith--")
    sleep(1)
    print("*Smith lands a cheap shot, and Morpheus falls onto the toilet*")

def stamina(stam):
    stam = input("Do you have enough stamina to fight? Y//N?\n")
    if stam in ['Y','y',"Yes","yes"]:
        morpheusTwo()
    else:
        print("recharging stamina!!!")
        stamina(stam)  

def morpheusTwo():        
    sleep(1)
    print("He gets up and dodges most of Smith's punches")
    sleep(1)
    print("o( -`д´-｡)o")
    sleep(2)

def defense(dodge):
    dodge = input("Will Morpheus be able to dodge Smith's attacks? Y//N?\n")
    if dodge in ['Y','y',"Yes","yes"]:
        morpheusThree()
        morpheusFour()
    else:
        morpheusFour() 

def morpheusThree():                  
    print()
    print("For his last move, Morpheus dodges Smith's last punch by jumping on the wall")
    sleep(1)
    print("______   ______")
    print("      \O/    ")
    print(" _____\|/______")
    sleep(2)

def morpheusFour():    
    print("***With nowhere to go, Morpheus unsuccessfully dodges Smith's grab***")
    print("**Smith grabs Morpheus by the leg and throws him onto the floor**")
    print("-(」゜ロ゜)」 -urrggh -ughhg -arrghh-")
    sleep(2)
    print("Agent Smith walks away and the police take Morpheus")
    sleep(2)
    print('~~~~~~~~*END*~~~~~~~')
    sys.exit

main()

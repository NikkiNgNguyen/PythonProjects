'''
Cesar Aleman
Judy Li
Winn Moo
Nikki Nguyen
Leonard Waxdeck
Group 4
12/9/15
Elleni Wolde

'''




import os
from time import sleep

def startScreen():
    print("================================================================================================")
    print(  "$$$$$$$$\ $$\                       $$\      $$\            $$\               $$\"          ")
    print(  "\__$$  __|$$ |                      $$$\    $$$ |           $$ |              \__|          ")    
    print(  "   $$ |   $$$$$$$\   $$$$$$\        $$$$\  $$$$ | $$$$$$\ $$$$$$\    $$$$$$\  $$\ $$\   $$\ ")
    print(  "   $$ |   $$  __$$\ $$  __$$\       $$\$$\$$ $$ | \____$$\\_$$  _|  $$  __$$\ $$ |\$$\ $$  |")
    print(  "   $$ |   $$ |  $$ |$$$$$$$$ |      $$ \$$$  $$ | $$$$$$$ | $$ |    $$ |  \__|$$ | \$$$$  / ")
    print(  "   $$ |   $$ |  $$ |$$   ____|      $$ |\$  /$$ |$$  __$$ | $$ |$$\ $$ |      $$ | $$  $$<  ")
    print(  "   $$ |   $$ |  $$ |\$$$$$$$\       $$ | \_/ $$ |\$$$$$$$ | \$$$$  |$$ |      $$ |$$  /\$$\ ")
    print(  "   \__|   \__|  \__| \_______|      \__|     \__| \_______|  \____/ \__|      \__|\__/  \__|")
    print("================================================================================================")

    print("This scene takes place right after Neo sees a glitch in the Matrix.")
    main()

def main():
    print("For Cypher, press 1.")
    print("For Trinity, press 2.")
    print("For Agent Smith, press 3.")
    print("For Neo, press 4.")
    print("For Morpheus, press 5.")

    character = int(input("Who do you choose?"))
    while character < 1 or character > 5:
        print("Sorry that is an invalid selection, please choose a number from 1-5")
        character = int(input("Who do you choose?"))
    characterSelection(character)

def characterSelection(character):
    if character == 1:
        print("You choose Cypher")
        cypher()
    elif character == 2:
        print("You choose Trinity")
        trinity()
    elif character == 3:
        print("You choose Agent Smith")
        agent()
    elif character == 4:
        print("You choose Neo")
        neo()
    elif character == 5:
        print("You choose Morpheus")
        morpheus()

def loop():
    print("Do you want to play again? Y/N")
    answer = input()
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        print("You said ", answer)
        main()
    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
        print("You said ", answer, "! Catch you on the flip side.")
    else:
        print("You said neither.")

###############################################################################################################
def cypher():
    pharse1 = "This scene takes place after Morpheus has been captured. Cypher has betrayed the team, but they still do not know. Scene begins in 3 seconds..."
    for i in range(len(pharse1)):
        print(pharse1[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse2 = "Phone rings..."
    for i in range(len(pharse2)):
        print(pharse2[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse3 = "Tank answers the phone and is surprised to find Cypher on the other end. Cypher tells him their was a car accident and he needs a way out."
    for i in range(len(pharse3)):
        print(pharse3[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse4 = "Trinity calls Tank and finds out they she and the others are not with Cypher."
    for i in range(len(pharse4)):
        print(pharse4[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse5 = "Cypher finds the old repair shop and the phone is ringing. He picks up the phone and is taken back to the ship."
    for i in range(len(pharse5)):
        print(pharse5[i], end="")
        sleep(.03)
    sleep(3)


    print()
    print()

    pharse6 = "Cypher regroups with Tank and asks how everyone is doing, Tank tells him that he is about to make the call."
    for i in range(len(pharse6)):
        print(pharse6[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse7 = "Cypher then gets a gun that was wrapped in a blanket. He takes aim at Tank and shoots!"
    for i in range(len(pharse7)):
        print(pharse7[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    zap1 = "------>>>>----->>>>----->>>>"
    for i in range(len(zap1)):
        print(zap1[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse8 = "He misses and Tank quickly gets up from his chair. But it is too late and Cypher already has another shoot loaded."
    for i in range(len(pharse8)):
        print(pharse8[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    zap2 = "------>>>>----->>>>----->>>>"
    zap3 = "------>>>>----->>>>----->>>>"
    for i in range(len(zap2)):
        print(zap2[i], end="")
        sleep(.02)
    sleep(1)

    print()
    print()

    for j in range(len(zap3)):
        print(zap3[j], end="")
        sleep(.02)
    sleep(3)

    print()
    print()

    pharse10 = "Dozer realizes what is happening and he runs after Cypher, but cypher fires before he could reach him."
    for i in range(len(pharse10)):
        print(pharse10[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse11 = "Now Cypher calls Trinity and she asks where Tank is, but now she knows what he has done."
    for i in range(len(pharse11)):
        print(pharse11[i], end="")
        sleep(.03)
    sleep(3)

    print()
    print()

    pharse12 = "****************************************END*******************************************"
    for i in range(len(pharse12)):
        print(pharse12[i], end="")
        sleep(.03)
    sleep(3)
    
    loop()

############################################################################################################################
def trinity():
    print("You have chosen Trinity.")
    sleep(1)
    print("Neo notices a glitch in the matrix.")
    sleep(1)
    print("*Trinity starts questioning Neo.*")
    sleep(1)
    print("*Trinity explains what happens when a glitch in the matrix occurs.*")
    sleep(1)
    print("Trinity begins running up the stairs.")
    sleep(1)
    print("She hands Morpheus her cellphone so that the group can escape.")
    sleep(1)
    print("She and the rest of the group begin scaling down the two walls.")
    sleep(1)
    print("As Morpheus attacks Agent Smith, Morpheus tells the rest of the group to escape.")
    sleep(1)
    print("Neo wants to stay behind to help Morpheus, but Morpheus says to run.")
    grabNeo()
    

def grabNeo():
    grab = 0
    grab = input("Do you want to grab Neo? Y/N")
    if grab == "Yes" or grab == "yes" or grab == "Y" or grab == "y":
        print("Success! Neo reluctantly leaves.")
        sleep(1)
        print("Trinity leads the group into a sewer to escape.")
        loop()
    elif grab == "No" or grab == "no" or grab == "N" or grab == "n":
        print("Neo doesn't want to go, do you want to try to grab him again?")
        grabNeo()

#############################################################################################################################              
def agent():
    print("You have selected the character Agent Smith. \n")
    sleep(1)
    print("")
    print("** Agent Smith is at The Lafayette Hotel searching for Morpheus and his crew **")
    sleep(2)
    print("")
    print("** Agent Smith hears something on his earpiece and pauses **")
    sleep(2)
    print("")
    print("He listens to the earpiece and tells the other agents that they are on the eighth floor")
    sleep(.5)
    print("")
    print("** A cop stops by a room and examines it and hears a cough through the walls**")
    sleep(1)
    print("")
    print("Agent Smith morphs into the policeman's body and takes over")
    print("")
    sleep(1)
    print("Agent Smith sticks his hands in the wall and grabs Neo. Morpheus sees and jumps through the wall and tackles the agent")
    sleep(1)
    print("")
    print("They both take turns throwing punches")
    sleep(1)
    fighting()
    print("Agent Smith slams Morpheus into the wall")
    print("")
    sleep(1)
    print("Morpheus gets back up and they continue fighting")
    print("")
    sleep(1)
    fighting()
    print("")
    print("Agent Smith kicks Morpheus and he hits his head on the toilet")
    print("")
    sleep(1)
    toilet()
    sleep(1)
    print("Morpheus and Agent Smith continue fighting")
    print("")
    print("")
    fighting()
    sleep(1)
    print("")
    print("Agent Smith punches Morpheus into the air")
    print("")
    sleep(1)
    fist()
    print("Agent Smith walks away and tells the agents to take him")
    loop()

def fighting():
    print("                __________                  __,___/  ',',")
    print("         ___.--'          '\'.         ____/  l   \    ','-,")
    print("  ------f''               // \\\       \  (l\ \    \     \ \',")
    print("        |                    |||       /   u       |      \ \ |")
    print("        |                    |||     _ )          /       | |  |")
    print("    ----L_-XXX-.             .|'    / U          <        | |  |")
    print("                '\   -<_____///     \           6 )       | |  |")
    print("                  \___)     -'       '.       -.<'       / /   |")
    print("                                      |'.___  |       _._.'   /")
    print("                                      |     ./     _.'.'   _.'")
    print("                                     /      |'----'     _.'")

def fist():

    print("   o   o")
    print("   k8 83,")
    print("  /\   /|")

def toilet():
    print("                  \     \.")
    print("                  |'\_____|")
    print("                  |` |    |")
    print("                  |  |    | ")
    print("     __-====-__  _|  |    |")
    print("    (~<       >~>  \ |    |")
    print("    !~~-====-~~/----`+----/")
    print("     \         \___     / ")
    print("      >------\     \  <  ")
    print("     <_________________>")



    
##############################################################################
def neo():
    print("You have selected Neo the Chosen One!!!!!\n")
    sleep(1)
    
    print('Neo and crew enter the Lafayette Hotel ')
    sleep(2)
    print('Neo is walking up the stairs ')
    sleep(2)
    print("*************Neo sees a black cat*************")
    sleep(3)
    print("*************Neo sees another black cat*************")
    sleep(2)
    print("-Whoa, deja vu.-")
    sleep(1)
    print('Trinity asks him what happened ')
    sleep(3)
    print("-A black cat went past us, and then another that looked just like it.-")
    sleep(3)
    print('Trinity explains that deja vu is a glitch in the Matrix which means something changed')
    sleep(3)
    print('Agents and Police kill Mouse')
    sleep(1)
    
    print(')-:')
    sleep(2)
    print('Morpheus takes Neo and the crew into a hole in the wall to hide from the agents')
    sleep(3)
    print('Morpheus tells Trinity to get Neo out and then attacks the agent')
    sleep(3)
    print('|\o/|')
    print('| | |')
    print('|/ \|')
    slide = input("press any button to escape from the agents and then press ENTER!")
    if slide != "":
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        sleep(1)
        print('|\o/|')
        print('| | |')
        print('|/ \|')
        sleep(1)
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        print('|   |')
        sleep(1)
        print('|\o/|')
        print('| | |')
        print('|/ \|')
    print('Neo survives')
    sleep(2)
    print('Police and Agents shoot at Neo, Trinity, and Apoc')
    sleep(1)
    print('They escape through a manhole')
    sleep(2)
    print('Neo and Trinity leave the hotel and try to find a hardline to leave the Matrix')
    sleep(2)
    print('**************END************')
    loop()

#########################################################################
def morpheus():
    stam = 0
    dodge = 0
    script()
    stamina(stam)
    defense(dodge)
    
def script():
    print("You have selected Morpheus!!!\n")
    sleep(1)
    print("****Morpheus' big battle****")
    sleep(1)
    print('***Morpheus, Trinity, Cypher, and Neo hide inside the wall behind the bathroom from the agents and police***')
    sleep(2)
    print('**Morpheus notices that Agent Smith grabbed Neo through the wall!**')
    sleep(2)
    print()
    print('OOOOOOOOOOOOOOOH!!!!!!!')
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
    loop()


#########################################################
startScreen()
os.system("pause")

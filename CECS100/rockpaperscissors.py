import random
comp = random.randint(1,3)
user = input("enter rock, paper, or scissors: ")
print ("user: " + user)
rock = 1
paper = 2
scissors = 3

if user == "rock":
    user = rock
elif user == "paper":
    user = paper
elif user == "scissors":
    user = scissors

if comp == 1:
    print("comp: rock")
elif comp == 2:
    print("comp: paper")
elif comp == 3:
    print("comp: scissors")
    
if comp == user:
    print("tie")
elif comp == rock and user == paper:
    print("user wins")
elif comp == paper and user == scissors:
    print("user wins")
elif comp == scissors and user == rock:
    print("user wins")
elif user == rock and comp == paper:
    print("comp wins")
elif user == paper and comp == scissors:
    print("comp wins")
elif user == scissors and comp == rock:
    print("comp wins")
    

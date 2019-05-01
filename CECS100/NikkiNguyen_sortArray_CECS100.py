'''
Student Name: Nikki Nguyen
Professor Name: Elleni Wolde
Class: CECS 100
Date: 11/16/2015
'''
import sys

def main():
    #declare
    name = 0
    nameList = [] 
    maxLengthList = 20
    #call methods
    greeting()
    getNames(nameList,maxLengthList)
    sortNames(nameList)
    userChoice = 'Y'
    sortAgain(userChoice,nameList,maxLengthList)
    
def greeting():
    print("Welcome to the Sorting Program!" '\n' "Enter a list of 20 names to be alphabetically sorted!")
    print()

def getNames(nameList,maxLengthList):
    #get 20 names
    while len(nameList) < maxLengthList:
        name = str(input("Enter one name at a time: "))
        #input validation, letters only
        while not name.isalpha():
            print("Invalid Input! Enter letters only!")
            name = str(input("Enter one name at a time: "))
        nameList.append(name)
        print(name)
    print("List of unsorted names:")
    print(nameList)

#sort names alphabetically
def sortNames(nameList):
    nameList.sort()
    print("List of sorted names:")
    print(nameList)
    return nameList

#run program until ready to quit
def sortAgain(userChoice,nameList,maxLengthList):
    userChoice = str(input("Do you want to restart? Enter Y//y or N//n: \t"))
    while userChoice not in ['Y','y','N','n']:
        print("Invalid Input! Please try again.")
        userChoice = str(input("Do you want to restart? Enter Y//y or N//n: \t"))
    if ((userChoice == 'Y') or (userChoice == 'y')):
        del nameList[:] 
        getNames(nameList,maxLengthList)
        sortNames(nameList)
        sortAgain(userChoice,nameList,maxLengthList)
    if ((userChoice == 'N') or (userChoice == 'n')):
        print("End of Sorting Program! \n")
        sys.exit()
        print()

#calling to main method
main()
    

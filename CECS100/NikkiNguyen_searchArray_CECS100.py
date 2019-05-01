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
    nameSearch = 0
    nameList = [] 
    maxLengthList = 20
    #call methods
    greeting()
    getNames(nameList,maxLengthList)
    findName(nameList,maxLengthList)
    userChoice = 'Y'
    searchAgain(userChoice,nameList,maxLengthList)
        
def greeting():
    print("Welcome to the Searching Program!")
    print()
    print("Enter a list of 20 names and" '\n' "you may search for a specific name from that list!")
    print()
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
        print(nameList)

#search through array
def findName(nameList,maxLengthList):
    nameSearch = str(input("Enter name to search from the list of 20:\t"))
    if nameSearch in nameList:
        print("Yes,",nameSearch,"is in the array")
    else:
        print("No,",nameSearch,"is not in the array")

#run program until ready to quit
def searchAgain(userChoice,nameList,maxLengthList):
    userChoice = str(input("Do you want to search for another name? Enter Y//y or N//n: \t"))
    while userChoice not in ['Y','y','N','n']:
        print("Invalid Input! Please try again.")
        userChoice = str(input("Do you want to search for another name? Enter Y//y or N//n: \t"))
    if ((userChoice == 'Y') or (userChoice == 'y')):
        findName(nameList,maxLengthList)
        searchAgain(userChoice,nameList,maxLengthList)
    if ((userChoice == 'N') or (userChoice == 'n')):
        userChoice = str(input("Do you want to restart from the very beginning? Program will end if N//n. Enter Y//y or N//n: \t"))
        while userChoice not in ['Y','y','N','n']:
            print("Invalid Input! Please try again.")
            userChoice = str(input("Do you want to restart from the very beginning? Program will end if N//n. Enter Y//y or N//n: \t"))
        if ((userChoice == 'Y') or (userChoice == 'y')):
            #remove contents of the list
            del nameList[:] 
            getNames(nameList,maxLengthList)
            findName(nameList,maxLengthList)
            searchAgain(userChoice,nameList,maxLengthList)
        if ((userChoice == 'N') or (userChoice == 'n')):
            print("End of Searching Program! \n")
            sys.exit()
            print()
            
#calling to main method
main()

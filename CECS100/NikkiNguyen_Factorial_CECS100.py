'''
Student Name: Nikki Nguyen
Professor Name: Elleni Wolde
Class: CECS 100
Date: 12/2/2015
'''
import sys

def main():
    n = getInput()
    inputValidation(n)
    recurFactorial(n)
 #   restart(userChoice)

def getInput():
    # take input from the user
    n = int(input("Enter a number: "))
    return n

def recurFactorial(n):
    #Function to return the factorial of a number using recursion
    if n == 1:
        return n
    else:
        return n*recurFactorial(n-1)

def inputValidation(n):
    # check is the number is negative
    if n < 0:
       print("Invalid Input, Enter numbers greater than or equal to 0")
       n = getInput()
       #recurFactorial(n)
    elif n == 0:
       print("The factorial of 0 is 1")
    else:
       print("The factorial of",n,"is",recurFactorial(n))
    restart()

def restart():
    userChoice = str(input("Do you want to get the factorial of another number? Enter Y//y or N//n: \t"))
    while userChoice not in ['Y','y','N','n']:
        print("Invalid Input! Please try again.")
        userChoice = str(input("Do you want to get the factorial of another number? Enter Y//y or N//n: \t"))
    if ((userChoice == 'Y') or (userChoice == 'y')):
        n = getInput()
        recurFactorial(n)
        inputValidation(n)
    if ((userChoice == 'N') or (userChoice == 'n')):
        print("End of Factorial Program! \n")
        sys.exit()
        print()
                         
#calling to main method                         
main()

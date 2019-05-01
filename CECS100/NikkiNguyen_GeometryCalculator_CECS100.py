'''
Student Name: Nikki Nguyen
Professor Name: Elleni Wolde
Class: CECS 100
Date: 10/13/2015
'''
import sys
#declare constants
PI = 3.14159
HALF = .5

#The main menu for the geometry calculator
def displayMenu():
    selection = 0
    print("         Geometry Calculator")
    print()
    print("----------------------------------------")
    print("| 1. Calculate the Area of a Circle    |")
    print("| 2. Calculate the Area of a Rectancle |")
    print("| 3. Calculate the Area of a Triangle  |")
    print("| 4. Quit                              |")
    print("| Enter your choice (1-4)              |")
    print("----------------------------------------")
    print()
    selection = int(input("Please choose calculate type or 4 to quit:"))
    return selection

#if else
def userChoice(selection):
    r = 0
    length = 0
    width = 0
    base = 0
    height = 0
    if selection == 1:
        r = int(input("Enter radius of circle: "))
        print("Area of circle is: ", PI*(r**2))
    elif selection == 2:
        length = int(input("Enter length of rectangle: "))
        width = int(input("Enter width of rectangle: "))
        print("Area of rectangle is: ", length*width)
    elif selection == 3:
        base = int(input("Enter length of triangle's base: "))
        height = int(input("Enter height of triangle: "))
        print("Area of triangle is: ", base*height*half)
    elif selection == 4:
        sys.exit()
    else:
        print("Error: Enter values 1-4 only")
        displayMenu()
        
        

#main function definition
def main():
    selection = displayMenu()
    userChoice(selection)
    
main()

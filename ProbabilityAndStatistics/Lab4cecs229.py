from math import sqrt
#Task 1
print("Task 1")
print("solution 1/2/3 all in one")
m = range(20)
def evenSquare(s):
    if s % 2 == 0:
        return s
list1 = filter(evenSquare,m)
list2= []
for x in list1:
    list2.append(x * x)
print(list(list2))

#Task 2
m = 20
print("\nTask 2")
print("solution 1/2/3 all in one")
fRange = range(m)
x = 1
y = 50
def F(n):
    if n < 2:
        return n
    return F(n - 1) + F(n - 2)
fList = [F(i) for i in fRange]
fibo = list(filter(lambda z : z > x and z < y, fList))
print(fibo)

#Task 3
print("\nTask 3")
print("no solutions work, 1 needs to print and return list, 2/3 there needs to be a fixed range")
nameList = ["Wendy", "Stan", "Mabel", "Dipper", "Soos", "Gideon"]
for name in nameList:
    print(len(name))
    
#Task 4
import itertools
print("\nTask 4")
print("no solutions work, 1 needs to print and return list, 2/3 there needs to be a fixed range")
foodList = ["primavera", "spaghetti", "alfredo", "carbonara", "marinara"]
drinkList = ["bang", "monster", "killcliff", "venom", "fourloko"]
foodDrinkList = list((x,y) for x in foodList for y in drinkList)
print(foodDrinkList)

#Task 5
print("\nTask 5")
print("solution 1/2/3 all in one")
range1 = range(1,20)
print("solution 3")
def pythagorean(a,b,c):
    if a > 0 in range1:
        return a
    if b > 0 in range1:
        return b
    if c > 0 in range1:
        return c
pyth = [(a,b,sqrt(a**2 + b**2)) for a in range1 for b in range1]
pyth = list(filter(lambda triple: triple[2].is_integer(), pyth))
print(pyth)


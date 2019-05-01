#Preliminary tasks

#a
string1 = "String"
list1 = [0,1,2,3,4,5]
tuple1 = (0, "one", 2, "a", 4.20)
set1 = {1,2,3,4}

#b
a = 11
b = 6
m = 5
print("b")
if (a - b) % m == 0:
    print ("congruent")
else:
    print ("not congruent")

#c
i = range(0,10)
congruent = list(filter(lambda x: x % 2 == 0, i))
print("\nc")
print (congruent)

#d
id = 14682900
list2 = [0,1,2]
m2 = 3
print("\nd")
for i in list2:
    if (id - i) % m2 == 0:
         print ("congruent")
    else:
        print ("not congruent")

#task B.1 (0)
list3 = [20,10,15,75]
print("\nB.1")
print(sum(list3) / float(len(list3)))

#task B.2 (0)
list4 = ['A','B','C']
list5 = [1,2,3]
result = []
for x in list4:
    for y in list5:
        result.append((x,y))
print("\nB.2")
print(result)

#task B.3 (0)
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
sumAll = sum([sum([x for x in inner_list]) for inner_list in  LofL])
print("\nB.3")
print(sumAll)

#task B.4 (0)

S = {-4,-2,1,2,5,0}
sumList = [(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0]
print("\nB.4")
print(sumList)

#task B.5 + B.6 (0)
S = {-4, -2, 1, 2, 5, 0}
noZeroSumList = [(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0 and not (x == 0 and y == 0 and  z == 0 )]
print("\nB.5")
print(noZeroSumList)
print("\nB.6")
firstTuple = [(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0 and not (x == 0 and y == 0 and  z == 0 )][0]
print(firstTuple)
print("The order of the elements in a set is not preserved because the order is not enforced, whereas lists and tuples are.")


#task B.6 (0)
oddNum = {x for x in range(1, 100) if x % 2}
print("\nB.6")
print(oddNum)


#task B.7 (0)
lastListA = [10, 25, 40]
lastListB = [1,15,20]
lastListZip = [a[0] + a[1] for a in zip(lastListA, lastListB)]
print("\nB.7")
print(lastListZip)

# Part A Part APart A Part A.
# Write a function called Quick_select to find the kth least element on a given array. (The average running time of your algorithm should be O(n)) (Hint: Use partitioning algorithm)
# 1. Request the user to enter a positive integer, and call it n.
# 2. Generate n random integers between -100 to 100 and save them in array a. (You can use randi function in MATLAB)
# 3. Print the generated array.
# 4. Request the user to enter a number between 1 to n (as the kth least element).
# 5. Call your function to find and print the kth least element.
# Part Part Part B.
# Explain an algorithm to return the max k numbers from an unsorted array. (The average running time of your algorithm should be O(n)) (Hint: You could modify your Quick_select algorithm to solve this question.)
# when you partition the pivot, left will be lower than the pivot and greater on the right
# once the array is partitioned so that values on the right of the pivot are greater than the pivot, so every number after the pivot
# will be the max k numbers

import random

def main():
    a = []
    n = int(input("enter a positive integer: "))
    for i in range(n):
        a.append(random.randint(-100,100))
    print(a)
    while True:
        print("1) find kth least element")
        print("2) find max k numbers")
        u = int(input("please pick 1 or 2: "))
        if u == 1:
            try:
                minK = int(input("enter a number between 1 and n: "))
                quick_select_min(a,0,len(a)-1,minK)
                print(quick_select_min(a,0,len(a)-1,minK))
            except ValueError:
                break
        if u == 2:
            try:
                maxK = int(input("enter a number between 1 and n: "))
                maxKInput = (len(a)-maxK)
                maxKIndex = quick_select_max(a,0,len(a)-1,maxKInput)
                for i in range (maxKInput,len(a)):
                    print("index: ", i)
                    print(a[i])
            except ValueError:
                break

def quick_select_min(a,start,end,k):
    #check if out of bounds
    if (k < 1 or k > len(a)):
        return None
    #if low is the same as high return leftmost position
    if(start == end):
        return a[start]

    median(a,start,end)
    pivotI = (start + end)//2 #pivot is median of three
    pivotVal = a[pivotI]  # element at pivot
    i = start #left
    j = end #right
    while (i <= j):  # while start is smaller than end
        while (a[i] < pivotVal):  # if the value of left is smaller than pivot, increment
            i += 1
        while (a[j] > pivotVal):  # if the value of the right is larger than pivot, decrement
            j -= 1
        if (start <= end):  # if the left is smaller than or equal to the right, swap values and go towards the middle
            swap(a, i, j)
            i += 1
            j -= 1  # pivot will be left index
    #check the k to the size of the left subarray
    aLow = pivotI - start + 1

    if (aLow == k):
        return a[pivotI]
    #recursion, while the left is greater than the k
    elif (aLow > k):
        return quick_select_min(a,start,pivotI - 1,k) #left subarray
    #if the right is less than the k
    else:
        return quick_select_min(a,pivotI + 1,end, k - aLow) #right subarray

def quick_select_max(a,start,end,k):
    #check if out of bounds
    if (k < 1 or k > len(a)):
        return None

    #if low is the same as high return leftmost position
    if(start == end):
        return start

    median(a,start,end)
    pivotI = (start + end)//2 #pivot is median of three
    pivotVal = a[pivotI]  # element at pivot
    i = start #left
    j = end #right
    while (i <= j):  # while start is smaller than end
        while (a[i] < pivotVal):  # if the value of left is smaller than pivot, increment
            i += 1
        while (a[j] > pivotVal):  # if the value of the right is larger than pivot, decrement
            j -= 1
        if (start <= end):  # if the left is smaller than or equal to the right, swap values and go towards the middle
            swap(a, i, j)
            i += 1
            j -= 1  # pivot will be left index
    #check the k to the size of the left subarray
    aHigh = pivotI - start + 1

    if (aHigh == k):
        return aHigh
    #recursion, while the left is greater than the k
    elif (aHigh > k):
        return quick_select_min(a,start,pivotI - 1,k) #left subarray
    #if the right is less than the k
    else:
        return quick_select_min(a,pivotI + 1,end, k - aHigh) #right subarray

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def median(a,start,end):
    # input low mid high in a new array
    b = []
    low = a[start]
    mid = a[(start + end)//2]
    high = a[end]
    b.append(low)
    b.append(mid)
    b.append(high)
    b = sorted(b)
    a[start] = b[0]
    a[(start + end) // 2] = b[1]
    a[end] = b[2]

main()

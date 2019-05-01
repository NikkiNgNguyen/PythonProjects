# Create two functions named quick_sort(a) and insertion_sort(a).
# 1. Request the user to enter a positive integer, and call it n.
# 2. Generate n random integers between -7000 to 7000 and save them in array a.
# 3. Call quick_sort(a) function to sort the array.
# 4. Call insertion_sort(a) function to sort the array.
# 5. Determine the average-running time of each function for n=10000, and 100 repetitions.
# 6. Calculate the growth of each function. (On a scratch paper!)
# 7. Calculate how many instructions your machine can run in a second using step 5 and 6(using the running time of insertion sort).
import time
import random
import math


def main():
    a = []
    s = 0
    r = 10  #repetitions
    n = 100
    # 1. request the user to enter a positive integer, and call it n.
    #n = (int(input("Enter a positive integer: ")))
    for j in range(n):
        a.append(random.randint(-7000, 7000))
    for i in range(s,r):
        # 2. Generate n random integers between -7000 to 7000 and save them in array a.
        temp = a[:] #slice array 
        startQuick = time.time()
        # 3. Call quick_sort(a) function to sort the array.
        quick_sort(temp,0,len(temp)-1)
        elapsedQuick = time.time()
        elapsedQuick += (elapsedQuick - startQuick)
    averageQuick = elapsedQuick/r
    #T(n) * singleLine = totalTime
    singleLineTimeQ = averageQuick/n*math.log2(n)
    nSingleLineQ = 1/singleLineTimeQ
    print("quick sort average running time: ", averageQuick)
    print("quick sort lines in a second: ", nSingleLineQ)

    for i in range(s,r):
        temp = a[:] #slice array
        #print(temp)
        startInsert = time.time()
        # 3. Call insertion_sort(a) function to sort the array.
        insertion_sort(temp)
        elapsedInsert = time.time()
        elapsedInsert += (elapsedInsert - startInsert)
    averageInsert = elapsedInsert / r
    singleLineTimeI = averageInsert/n**n
    nSingleLineI = 1/singleLineTimeI
    print("insertion sort average running time: ", averageInsert)
    print("insertion sort lines in a second: ", nSingleLineI)




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

def quick_sort(a,start,end): #O(log n) conquer 
    if start < end: #once cross then finish
        median(a,start,end) #swap place of start/mid/end
        piv = partition(a,start,end) #get pivot
        if(start < piv - 1):
            quick_sort(a,start,piv-1) #left of pivot
        if(piv < end):
            quick_sort(a,piv,end) #right of pivot

def partition(a,start,end): #O(n) divide
    pivot = (start + end) // 2 # gives pivot index, and will be the median
    pivotVal = a[pivot]   #element at pivot
    left = start
    right = end
    while (left <= right):   #while start is smaller than end
        while (a[left] < pivotVal):   #if the value of left is smaller than pivot, increment
            left += 1
        while(a[right] > pivotVal):   #if the value of the right is larger than pivot, decrement
            right -= 1
        if(left <= right ):           #if the left is smaller than or equal to the right, swap values and go towards the middle
          swap(a,left,right)
          left+=1
          right-=1                    #pivot will be left index
    pivot = left
    return pivot

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def insertion_sort(c): #O(n^2)
    for i in range(1,len(c)): #show loop invariant (true prior to 1st iteration, true before next iteration, loop terminates)
        key = c[i] #set key
        j = i - 1 #first element to left of i
        while (j >= 0 and key < c[j]): #index at least 0, and element at i > key
            c[j + 1] = c[j] #shift right
            j = j - 1 #first iteration = -1
        c[j + 1] = key #swap key to the left (if break after first iteration, -1 + 1 = 0, move element to index 0)


main()


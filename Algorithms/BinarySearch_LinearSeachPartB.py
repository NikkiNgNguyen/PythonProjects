'''
Part B. In this part we will calculate the worst-case running time of each function.
1. Repeat steps 1 to 3 in part A.
2. Now to have the worst-case scenario, set the value of the key to 5000 to make sure it does not exist in the array.
3. Run each function once to calculate the worst-case running time when n = 105.
4. Calculate how much time your machine takes to run one single step. (Hint: look at HW3)
5. Now estimate the worst-case running time for each algorithm when n=107. (Hint: look at HW3)
6. Now repeat step 1-3 for n = 107 and compare the actual running time with your answer in step 5.
'''
import random
import time
import math

def partA():
    x = 0
    m = 0
    a = []
    n = 100000 #10^7
    key = 5000
    n = int(input("Enter a positive integer: "))
    for i in range(n):
        a.append(random.randint(-1000,1000))
    #print("unsorted: ")
    #print(a)
    #print("sorted: ") #timsort: hybrid sorting algorithm derived from merge sort and insertion sort
    a.sort()
    #print(a)

    print("linear search single line time: ")
    start_linear = time.time()
    linearSearch(a,key)
    elapsed_linear = (time.time() - start_linear)/n
    print(elapsed_linear)
    print()
    print("binary search single line time: ")
    start_binary = time.time()
    binarySearch(a,key)
    elapsed_binary = (time.time() - start_binary)/math.log2(n)
    print(elapsed_binary)

def linearSearch(a,key):
    for i in range(len(a)):
        if a[i] == key:
            #print("key found", key)
            return key
    print("key not found")
    return -1

def binarySearch(a,key):
    low = 0
    high = len(a)-1
    found = False
    while(low <= high and not found): 
        middle = (low + high)//2
        if (a[middle] == key):
            found = True
            #print("key found: ", key)
        else:
            if (key < a[middle]):
                high = middle - 1
            else:
                low = middle + 1
        print("key not found")
        return -1

def main():
    partA()

main()

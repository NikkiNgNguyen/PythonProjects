'''
Part A. In this part we will calculate the average-case running time of each function.
1. Request the user to enter a positive integer, and call it n. (n = 10^5)
2. Generate n random integers between -1000 to 1000 and save them in array a. (You can use randi function in MATLAB)
3. Sort a (you can use any sorting algorithm you want. If you are using MATLAB, you can call the sort function to sort your numbers)
4. Pick a random number in a and save it in variable called key.
5. Call each function separately to search for the key in the given array.
6. To calculate the average-running time, you need to have a timer to save the total runtime when repeating step 4 and 5 for 500 times. (tic toc in MATLAB)
(Note1: Do not forget to divide the runtime by the number of the times you run step 4-5)
(Note2: Remember to choose a different random number each time you go back to step 4.)

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
    n = 0
    n2 = 100000 #10^5
    n3 = 10000000 #10^7
    key = 0

    n = int(input("Enter a positive integer: "))
    for i in range(n):
        a.append(random.randint(-1000,1000))
    #print("unsorted: ")
    #print(a)
    #print("sorted: ") #timsort: hybrid sorting algorithm derived from merge sort and insertion sort
    a.sort()
    #print(a)
    print("linear search average time: ")
    start_linear = time.time()
    while(x<=500):
        key = random.choice(a)
        linearSearch(a,key)
        x = x + 1
    elapsed_linear = (time.time() - start_linear)/500
    print(elapsed_linear)
    print()
    print("binary search average time: ")
    while(m<=500):
        start_binary = time.time()
        key = random.choice(a)
        binarySearch(a,key)
        m = m + 1
    elapsed_binary = (time.time() - start_binary)/500
    print(elapsed_binary)
        
    print()
    key = 5000
        
    print("linear search single line time 10^5: ")
    start_linear = time.time()
    linearSearch(a,key)
    #single line
    elapsed_linear = (time.time() - start_linear)/n2 #(O(n))
    print(elapsed_linear)
    print()
        
    print("binary search single line time 10^5: ")
    start_binary = time.time()
    binarySearch(a,key)
    #single line
    elapsed_binary = (time.time() - start_binary)/math.log2(n2) #(O(logn))
    print(elapsed_binary)

    print()
    print("linear search estimate 10^7: ")
    est_single_lineL = elapsed_linear * n3
    print(est_single_lineL)
    print()
    print("linear search estimate 10^7: ")
    est_single_lineB = elapsed_binary * math.log2(n3)
    print(est_single_lineB)
    print()
    
    print("linear search single line time 10^7: ")
    start_linear = time.time()
    linearSearch(a,key)
    #single line
    elapsed_linear = (time.time() - start_linear)/n3
    print(elapsed_linear)
    print()
        
    print("binary search single line time 10^7: ")
    start_binary = time.time()
    binarySearch(a,key)
    #single line
    elapsed_binary = (time.time() - start_binary)/math.log2(n3)
    print(elapsed_binary)



def linearSearch(a,key):
    for i in range(len(a)):
        if a[i] == key:
            #print("key found", key)
            return key
    #print("key not found")
    return -1

    
def binarySearch(a,key):
    low = 0 #first element
    high = len(a)-1 #last element
    found = False #possible to return true or false
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
        #print("key not found")
        return -1


def main():
    partA()


main()

# Write 2 functions to calculate the MSS of a given array one with running time of O(n) and one with O(nlogn).
# Request the user to enter a positive integer, and call it n.
# 1. Generate n random integers between -100 to 100 and save them in array a. (You can use randi function in MATLAB)
# 2. Print the generated array and the outputs of your two functions.
import random
import math

def main():
    a = []
    n = int(input("enter a positive integer: "))
    for i in range(n):
        a.append(random.randint(-10, 10))
    print(a)
    print("MSS in O(n): ", mssN(a))
    print("MSS in O(nlogn): ", mssNlogN(a,0,len(a)-1))

def mssN(a):
    mss = 0
    temp = 0
    for i in range(0,len(a)):
        if temp + a[i] > 0:
            temp  = temp + a[i]
            if temp > mss:
                mss = temp
        elif a[i] + temp < 0:
            temp = 0
    return mss


def mssNlogN(a,low,high):
    mss = 0
    temp = 0
    leftSum = 0
    rightSum = 0
    #if the left is equal to the right, the mss will be the leftmost position
    if(low == high):
        mss = a[low]
    else:
        middle = (low + high) // 2
        mLeft = mssNlogN(a,low,middle) #split first half
        mRight = mssNlogN(a,middle + 1, high) #split left half
        for i in range(middle,low-1,-1): #start from the middle and go to the beginning
            temp += a[i] #iterate through
            if(temp > leftSum): #take the greater value
                leftSum = temp
        temp = 0
        for i in range(middle+1,high+1): #after the pivot to the end of the array
            temp += a[i] #iterate through
            if (temp > rightSum): #take the greater value
                rightSum = temp
        #the middle is the sum of the left and the right
        
        mMid = leftSum + rightSum
        #return the largest value
        mss = max(max(mLeft,mRight),mMid)
    return mss






main()

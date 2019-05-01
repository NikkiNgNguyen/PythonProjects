"""
Nikki Nguyen
CECS 328 Lab 5
April 20, 2018
Create three functions named build_MaxHeap(a), max_heapify(a,i), heap_sort(a).
1. Request the user to enter a positive integer, and call it n.
2. Generate n random integers between -10000 to 10000 and save them in array a.
3. Call heap_sort(a) function to sort the array. In order to sort the array using heapsort, you need to follow the below steps:
3.1 Build a max-heap (call the function build_heap(a)). In order to build the max-heap follow the below pseudocode:
% new_a is the output of the function, if you are using any other programming language, please write % return new_a at the end of your code.
a = build_MaxHeap(a)
n = length(a);
for i=n:-1:1 % i= n downto 1, Can we start from n/2 instead of n? Why????
% you have the pseudocode for max_heapify in the heap binary pdf file on beachboard
a = max_heapify(a,i);
end
3.2 Remove the root (remove the first element in a): In order to do that, follow the instructions in the heap binary pdf file on beachboard.
4. Determine the average-running time of heap_sort function for n=10000, and 100 repetitions.
5. Compare your answer with the average-running time of quicksort and selection sort (you need implement it).
"""
import random
import time

def main():
    #n = int(input("Enter a positive integer: "))
    #inputSize = 10000
    inputSize = int(input("Enter a positive integer: "))
    r = 100
    s = 0
    elapsedHeap = 0
    a = []
    for i in range(inputSize):
        a.append(random.randint(-10000,10000))
    print(a)
    heap_sort(a,inputSize)
    print(a)

    for i in range(s,r):
        a = []
        for i in range(inputSize):
            a.append(random.randint(-10000,10000))
        temp = []
        temp = a
        n = len(a)
        startHeap = time.time()
        heap_sort(temp,n)
        endHeap = time.time()
        elapsedHeap += (endHeap - startHeap)
    averageHeap = elapsedHeap/r
    print("Heap Sort running time: ", averageHeap)


def build_MaxHeap(a,n):
    #apply the max_heapify function starting from the last element in the tree and move upward til you reach 1
    for i in range(n,-1,-1):
        max_heapify(a,n,i)



def max_heapify(a,n,i):
    #root is the beginning
    max_index = i
    #left child
    left_index = (2*i + 1)
    #right child
    right_index = (2*i + 2)
    #if there is a left child and it is greater than the root 
    if left_index < n and a[left_index] > a[max_index]:
        max_index = left_index
    #if there is a right child and it is greater than the root
    if right_index < n and a[right_index] > a[max_index]:
        max_index = right_index
    if max_index != i:
        swap(a,max_index,i)
        max_heapify(a,n,max_index)


def heap_sort(a,n):
    #build a max heap
    build_MaxHeap(a,n)
    #remove the root and insert it to the last position in the array
    #repeat until empty
    for i in range(n-1,0,-1):
        swap(a,i,0)
        max_heapify(a,i,0)



def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    
main()

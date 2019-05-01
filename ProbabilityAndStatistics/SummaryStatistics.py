from collections import Counter
import math

# PART I: SUMMARY STATISTICS
# Get data from user input
# [3, 2, 4, 1, 2, 3, 4, 3, 5, 10]
numbers = []
while True:
    try:
        n = int(input('Enter a number to add to your data set.'))
        numbers.append(n)
    except ValueError:
        break
        
# Find the mean
s = sum(numbers)
N = len(numbers)
mean = s / N
print('Mean: ', mean)

# Find the median
numbers.sort()
if N % 2 == 0:
    p1 = N / 2
    p2 = (N /2) + 1
    p1 = int(p1) - 1
    p2 = int(p2) - 1
    median = (numbers[p1] + numbers[p2]) / 2
else:
    p = (N + 1) / 2
    p = int(p) - 1
    median = numbers[p]
print('Median: ', median)

# Find the mode
c = Counter(numbers)
mode = c.most_common(1)
m = mode[0][1]
if m == 1:
    print('There is no mode.')
else:
    print('Mode: ', m)

# Find the standard deviation
a = 0
for x in numbers:
    y = (x - mean) ** 2
    a = a + y
sigma = math.sqrt(a / N)
print('Standard Deviation: ', '%.4f'% sigma)


# PART II: RANDOM NUMBER GENERATOR
N = 10000
A = 4857
M = 8601
S = int(input('Enter a nonnegative integer for the seed'))
k = int(input('Enter the number of random numbers wanted'))
total = 0

for i in range(1, k + 1):
    S = (M * S + A) % N
    r = S / N
    total = total + r
    print(format('%.4f'% r))

Average = total / k
print('Mean: ', '%.4f'% Average)
    

# PART III: PROBABILITY PROBLEM
S = 0
Sum = 0
Can = [0, 0, 0]
K = int(input('Enter the number of experiments.'))

for k in range(K):
    for i in range(3):
        S = (M * S + A) % N
        r = S / N
        Can_Number = math.floor(r * 5 + 1)
        Can[i] = Can_Number
    if((Can[0] != Can[1]) & (Can[1] != Can[2]) & (Can[0] != Can[2])):
        Sum = Sum + 1

prob = Sum / K
print('The probability of the three balls in different cans is', prob)

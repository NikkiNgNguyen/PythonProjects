# Part 1: Bernoulli Trials
print("Part 1:")
import random
n = int(input('How many trials do you want to simulate?'))
p = float(input('What is the probability of a success?'))
for i in range(n):
    r = random.uniform(0, 1)
    if r < p:
        print('Success')
    else:
        print('Failure')

# Part 2: Bayes' Probability
print("\nPart 2:")
C = [0.0001, 0.001, 0.001, 0.0001, 0.001]
BC = [0.9, 0.9, 0.9, 0.95, 0.95]
BnotC = [0.001, 0.001, 0.01, 0.001, 0.01]

print("P(C|B):")
for i in range(len(C)):
    B = C[i] * BC[i] + BnotC[i] * (1 - C[i])
    CB = (C[i] * BC[i]) / B
    print(CB)

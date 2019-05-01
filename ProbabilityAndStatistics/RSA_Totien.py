'''
Nikki Nguyen
October 23, 2017
CECS 229
Lab 6
'''
import math

print("a. RSAsettings: set prime numbers (p, q)")
pNum = 61
qNum = 53
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
if isPrime(pNum) is True:
    p = pNum
if isPrime(qNum) is True:
    q = qNum
print(p)
print(q)
print()
    
print("b. Totien: calculate totien for given prime numbers")
def calcTotien(p,q):
    totien = (p - 1) * (q - 1)
    return totien
totien = calcTotien(p,q)
print(totien)
print()
    
print("c. EDExponent: calculate encryption-decryption exponent")
exponent = (totien * 15) + 1
print(exponent)
print()

print("d. PK_SKSettings: Assume the keys and check their validity")
pk = 17
sk = exponent/pk
n = p*q
def validatePK(num):
    if 1 < num and num < totien:
        return True
    else:
        return False
if validatePK(pk) is True:
    PK = pk
print(PK)
def validateSK(num):
    if ((num * pk ) % totien == 1):
        return True
    else:
        return False
if validateSK(sk) is True:
    SK = sk
print(SK)
print()

print("e. Encrypt: Return the cypher given the plaintext")
def encrypt(plaintext):
    cypher = (plaintext ** PK) % n
    return cypher
cypher = encrypt(123)
print(cypher)

print("f. Decrypt: Return the plaintext given the cypher")
def decrypt(cypher):
    SK = 2753
    cypherD = pow(cypher,SK,n)
    return cypherD
#smaller number
plaintext = decrypt(cypher)
print(plaintext)
print()

print("g. Exponentiation: Return the table of powers of 2 for a given number")
def powerFind(n):
    result = []
    binary = bin(n)[:1:-1]
    for x in range(len(binary)):
        if int(binary[x]):
            result.append(pow(2,x))
    return result
result = powerFind(2753)
print(result)

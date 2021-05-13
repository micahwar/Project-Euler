import math
#Truncatable Primes

def isPrime(n):
    if n == 2: return True
    if (n % 2) == 0 or n == 1:
        return False
    y = 3
    while y*y <= n:
        if (n % y) == 0:
            return False
        y = y + 2
    return True

def isTruncatable(n):
    n = str(n)    
    return isTruncatableRec(n, 1) and isTruncatableRec(n, -1)

def isTruncatableRec(n, d):
    if len(n) == 1:
        if isPrime(int(n)):
            return True
        else:
            return False
    if not isPrime(int(n)):
        return False
    else:
        if d == 1:
            return isTruncatableRec(n[1:], d)
        else:
            return isTruncatableRec(n[:-1], d)
print(isTruncatable(3797))
foundCount = 0
found = []
x = 10
while foundCount < 11:
    x += 1
    if not isPrime(x):
        continue
    if isTruncatable(x):
        foundCount += 1
        found.append(x)
        print(x)
    

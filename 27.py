import math
primes = defaultdict(bool)
def isPrime(num):
    if num < 0:
        return False
    for i in range(1, round(math.sqrt(num)), 1+(num%2)):
        if num % i == 0 and i != 1:
            return False
    return True
highest = 0
highestMult = 0
r = 1000
for a in range(-(r-1), r):
    for b in range(-r, r+1):
        n = -1
        while(isPrime((n**2) + (a*n) + b)):
            n += 1
        if n > highest:
            highest = n
            highestMult = a*b
print(highestMult)
        

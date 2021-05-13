import math, time
from itertools import product

def isPrime(nm):
    for i in range(1, round(math.sqrt(nm)), 1+(nm%2)):
        if nm % i == 0 and i != 1:
            return False
    return True

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def createMasks(length, count):
    masks = []
    for x in product(range(length), repeat=count):
        if allUnique(x):
            masks.append(x)
    return list(set(tuple(sorted(l)) for l in masks))

def applyMask(length, mask):
    nums = []
    antiMask = [y for y in range(length) if not y in mask]
    for x in product(range(10), repeat=(length-len(mask))):
        tnums = []
        if antiMask[0] != 0 or x[0] != 0:
            num = ["*"]*length
            for i, element in enumerate(x):
                num[antiMask[i]] = str(element)
            if num[len(num)-1] != "*":
                if int(num[len(num)-1]) % 2 != 0:
                    for rng in range(10):
                        if rng != 0 or not 0 in mask:
                            nnum = num
                            for element in mask:
                                nnum[element] = str(rng)
                            tnums.append("".join(nnum))
        nums.append(tnums)
    return nums

done = False
le = 0
now = time.time()
while not done:
    le += 1
    for r in range(1, le):
        for mask in createMasks(le, r):
            for Set in applyMask(le, mask):
                primes = [x for x in Set if isPrime(int(x))]
                if len(primes) == 8:
                    print(primes[0])
                    done = True
                    
print(time.time() - now)

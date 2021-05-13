import math, time, itertools
from numba import jit
now = time.time()

@jit
def isPrime(nm):
    for i in range(1, round(math.sqrt(nm)), 1+(nm%2)):
        if nm % i == 0 and i != 1:
            return False
    return True

def eratosthenes(n):
    a = [True]*n
    a[0] = a[1] = False
    for i in range(2, round(math.sqrt(n))):
        if a[i]:
            for j in range(i**2, n, i):
                a[j] = False
    return a

isPrimes = eratosthenes(9000)

primes = []
for i, prime in enumerate(isPrimes):
    if prime:
        primes.append(i)
isPrimes = eratosthenes(90009000)
print(time.time() - now)
rng = 5
first = [[], [], [], [], [], []]
first[0] = primes
limit = 100000000
for i in range(0, rng):
    if i == 0:
        for x in itertools.combinations(first[0], 2):
            x = [str(x_) for x_ in x]
            for g in itertools.permutations(x, 2):
                if int(g[0] + g[1]) < limit:
                    if isPrimes[int(g[0] + g[1])] and isPrimes[int(g[1] + g[0])]:
                        first[i+1].append(tuple(sorted((int(g[0]), int(g[1])))))
    else:
        #print(first[i])
        for x in first[i]:
            for prime in first[0]:
                isValid = True
                for element in x:
                    if not isPrimes[int(str(element) + str(prime))] or not isPrimes[int(str(prime) + str(element))]:
                        isValid = False
                        break
                    elif int(str(element) + str(prime)) > limit:
                        isValid = False
                        break
                if isValid:
                    newArr = [y for y in x]
                    newArr.append(prime)
                    first[i+1].append(tuple(sorted(newArr)))
    first[i+1] = list(set(first[i+1]))
    first[i+1].sort()

print(min([sum(x) for x in first[rng - 1]]))
print(time.time() - now)

import math
from collections import defaultdict

def getDivisors(n):
    count = []
    if n % 2 != 0:
        step = 2
    else:
        step = 1
    for i in range(1, round(math.sqrt(n)) + 1, step):
        if n % i == 0:
            if i != n/i:
                count.append(n/i)
            count.append(i)
            
    return sum(count) - n
abundants = []
maximum = 28124
for n in range(1, int(maximum)):
    if getDivisors(n) > n:
        abundants.append(n)

isValid = [False] * maximum
for j in abundants:
    for k in abundants:
        if j + k < maximum:
            isValid[j+k] = True

print(sum([i for i, num in enumerate(isValid) if num == False]))

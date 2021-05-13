from collections import defaultdict
import math
def isMultiPandigital(x, y, xy):
    return "".join(sorted(list(str(x)+str(y)+str(xy)))) == "123456789"

def old():
    product = defaultdict(bool)
    products = []
    for x in range(2000):
        for y in range(2000):
            if not product[x*y]:
                if isMultiPandigital(x, y, x*y):
                    product[x*y] = True
                    products.append(x*y)
    print(sum(products))

def hasMultiPandigitalFactors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            possPan = str(i) + str(n) + str(n//i)
            if "".join(sorted(possPan)) == "123456789":
                return True
    return False
def new():
    products = []
    for i in range(10000):
        if hasMultiPandigitalFactors(i):
            products.append(i)
    return (sum(products))

print(new())

highestSolutions = 0

def getChildren(trip=(3, 4, 5), perim=1000, primitive=1):
    

for p in range(1, 1001):
    num = getSolutions(p)
    if num > highestSolutions:
        highestSolutions = num
num = 100
squareofsum = sum([x for x in range(1, num + 1)]) ** 2
sumofsquare = sum([x ** 2 for x in range(1, num + 1)])
difference = squareofsum - sumofsquare
print(difference)

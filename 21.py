import math
amicable = []
def d(num):
    dvs = [1]
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            dvs.append(i)
            dvs.append(num/i)
    return sum(dvs)
for n in range(1, 10000):
    divs = d(n)
    divs2 = d(divs)
    if n == divs2 and n!= divs and not n in amicable:
        amicable.append(n)
        amicable.append(divs)
print(sum(amicable))
    
    

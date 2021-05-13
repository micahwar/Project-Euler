import itertools
total = 0

def getCombo(n):
    if n % 2 == 0:
        return n/2 + 1
    else:
        return (n+1) / 2
value = 200
for x in itertools.product(range(0, (int(value/5)+1)*5, 5), range(0, (int(value/10)+1)*10, 10), range(0, (int(value/20)+1)*20, 20), range(0, (int(value/50)+1)*50, 50), range(0, (int(value/100)+1)*100, 100), range(0, (int(value/200)+1)*200, 200)):
    x = sum(x)
    if x <= 200:
        total += getCombo(value - x)
print(total)
            
    

from time import time
now = time()
end = 1000000
n1 = 1
n2 = 2
answer = 2
while True:
    new = n1 + n2
    if new < 4000000:
        if new % 2 == 0:
            answer += new
        n1 = n2
        n2 = new
    else:
        break
print (answer)
print (time() - now)

start = 1
size = 1001
total = 1
for d in range(1, int((size-1)/2) + 1):
    for i in range(0, 4):
        start += (2*d)
        total += start
print(total)

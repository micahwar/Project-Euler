p = 1
fp = 1
f = 0
i = 2
while len(str(f)) < 1000:
    i += 1
    f = p + fp
    p = fp
    fp = f
    
print(i)

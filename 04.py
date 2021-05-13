def checkPalindrome(num):
    num = str(num)
    if (len(num) % 2) != 0:
        return False
    half = int(len(num)/2)
    if num[:half] == num[half:][::-1]:
        return True
    return False
best = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        xy = x * y
        if checkPalindrome(xy) == True:
            if xy > best:
                best = xy
print(best)

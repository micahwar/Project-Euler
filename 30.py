nums = []
for n in range(2, 200001):
    if sum([int(x)**5 for x in list(str(n))]) == n:
        nums.append(n)
print(nums)
print(sum(nums))

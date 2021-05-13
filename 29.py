nums = []
for a in range(2, 101):
    for b in range(2, 101):
        nums.append(a**b)
nums = sorted(list(set(nums)))
print(len(nums))

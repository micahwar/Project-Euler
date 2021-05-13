start = 1 # Monday
start_Year = 1900
count = 0
month_Lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for year in range(0, 101):
    if (start_Year + year) % 4 == 0 and year != 0:
        month_Lengths[1] = 29
    else:
        month_Lengths[1] = 28
    if year == 1:
        count = 0
    for month in range(0, 12):
        start += 1
        if start % 7 == 0:
            count += 1
        for day in range(2, month_Lengths[month]+1):
            start += 1
        
print(count)

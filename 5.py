done = False
count = 20
while done == False:
    doney = False
    for i in range(3, 20):
        if count % i != 0:
            doney = True
    if doney == False:
        print(count)
        break
    count += 20

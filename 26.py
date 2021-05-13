def getCycleLength(d, n, r, c, f, k, j):
    if (d in k):
        return (r - 1) - k.index(d)
    else:
        k.append(d)
        if not j:
            if d < n:
                d *= 10
        if d < n:
            f.append(0)
            return getCycleLength(d*10, n, r+1, n, f, k, True)
        else:
            m = 1
            while c+n <= d:
                c += n
                m += 1
            if c == d:
                return (0)
            else:
                f.append(m)
                return getCycleLength(d - c, n, r+1, n, f, k, False)
a = [int(getCycleLength(1, x, 1, x, [], [], False)) for x in range(1, 1000)]
print(a.index(max(a)) + 1)

from itertools import permutations
digits = "0123456789"
print(["".join(x) for x in list(permutations(digits))][999999])

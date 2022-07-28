from itertools import combinations
k1 = 0
k2 = 0
for x in combinations("123", r = 2):
    k1 += 1
for x in combinations("12345678", r = 2):
    k2 += 1
print(k1*k2)

from itertools import permutations
k = 0
for x in permutations("СМТБГ", r = 5):
    k += 1
print(k)

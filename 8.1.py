from itertools import product
k = 0
for x in product("012345", repeat = 6):
    x = "".join(x)
    if (x[0] != "0" and (x.count("0") + x.count("2") + x.count("4") == 2)):
        k += 1
print(k)

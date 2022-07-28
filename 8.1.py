from itertools import product
k = 0
for x in product("01", repeat = 9):
    x = "".join(x)
    if x.count("0") == 4 and x.count("1") == 5:
        if "00" not in x:
            k += 1
print(k)
    

from itertools import product
k = 0
for x in product("0123456789", repeat = 4):
 x = "".join(x)
 if "35" in x:
     if x[0] != "0" and int(x) % 3 == 0:
     k += 1
print(k)

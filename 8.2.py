from itertools import product
k = 0
count1 = 0
count2 = 0
for x in product("УЕВПСНЬ", repeat = 7):
    x = "".join(x)
    k += 1
    if x == "ВУПСЕНЬ":
        count1 = k
    if x == "ПУПСЕНЬ":
        count2 = k
print(count2-count1)
        

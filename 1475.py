import math
N = list(input())
max_count = 0

for i in range(9):
    if (i != 6):
        max_count = max(max_count,N.count(str(i)))
    else:
        max_count = max(max_count, math.ceil((N.count(str(i)) + N.count("9"))/2))


print(max_count)
import math
fixed, variable, price = list(map(int,input().split()))

if variable >= price:
    print(-1)
else:
    print(math.floor(fixed / (price - variable)+1))


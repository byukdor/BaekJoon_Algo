import math
X, Y = map(int,input().split())

current_ratio = int(Y * 100 / X)
low, high = 0, 1000000000
if current_ratio >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        dx = X + mid
        dy = Y + mid
        if int(dy * 100 / dx) > current_ratio:
            high = mid - 1
        else:
            low = mid + 1
    print(high + 1)
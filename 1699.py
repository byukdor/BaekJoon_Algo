import math
N = int(input())
dp = [0 for i in range(N + 1)]
square = [i ** 2 for i in range(1, math.ceil(math.sqrt(100000)))]

for i in range(1, N + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1

print(dp[N])
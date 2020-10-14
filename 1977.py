import math

M = math.ceil(int(input()) ** (1/2))
N = math.floor(int(input()) ** (1/2))
total = 0

if M < N:
    for i in range(M,N + 1):
        total += (i ** 2)
    print(total)
    print(M ** 2)
else:
    print(-1)



N = int(input())

for i in range(2,N+1):
    while (N > 1) & (N % i == 0):
        print(i)
        N = N // i
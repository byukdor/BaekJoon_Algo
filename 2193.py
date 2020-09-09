N = int(input())

ones = [0] * N
zeros = [0] * N

ones[0] = 1
zeros[0] = 0

for i in range(1,N):
    ones[i] += zeros[i - 1]
    zeros[i] = ones[i - 1] + zeros[i - 1]

print(ones[N-1]+zeros[N-1])
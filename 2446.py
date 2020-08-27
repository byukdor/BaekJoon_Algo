N = 2 * int(input()) - 1

for i in range(N, 1, -2):
    print(" " * ((N-i)//2) + "*" * (i))

for i in range(1, N+1, 2):
    print(" " * ((N-i)//2) + "*" * (i))
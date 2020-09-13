import sys

N = int(input())
count = 0

for i in range(N):
    multi = int(sys.stdin.readline())

    if i < (N - 1):
        count += (multi - 1)
    else:
        count += multi

print(count)

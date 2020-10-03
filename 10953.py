import sys
N = int(input())

for i in range(N):
    print(sum(map(int,sys.stdin.readline().rstrip().split(","))))
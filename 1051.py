import sys

N, M = map(int,input().split())
board = []
maximum = 0

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))


for i in range(N):
    for j in range(M):
        for k in range(min(N,M)):
            if i + k < N and j + k < M:
                if board[i][j] == board[i][j + k] == board[i + k][j] == board[i + k][j + k]:
                    maximum = max(maximum, (k + 1) ** 2 )

print(maximum)
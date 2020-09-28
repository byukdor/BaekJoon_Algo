import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0] * (N + 1) 
    visit[start] = 1
    count = 1
    while q:
        target = q.popleft()
        for i in cpu_list[target]:
            if visit[i] == 0:
                visit[i] = 1
                count += 1
                q.append(i)
    return count

N, M  = map(int,sys.stdin.readline().split())
cpu_list = [[] for i in range(N + 1)]

for i in range(M):
    x1, x2 = map(int,sys.stdin.readline().split())
    cpu_list[x2].append(x1)

result = []
maximum = 0
for i in range(1, N + 1):
    temp = bfs(i)
    if maximum == temp:
        result.append(i)
    elif maximum < temp:
        maximum = temp
        result = []
        result.append(i)

print(" ".join(map(str,result)))
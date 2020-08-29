N, M = list(map(int,input().split()))
cardList = list(map(int,input().split()))
highest = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if cardList[i] + cardList[j] + cardList[k] <= M:
                highest = max(highest, cardList[i] + cardList[j] + cardList[k])

print(highest)
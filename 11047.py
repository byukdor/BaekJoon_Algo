N, K = list(map(int,input().split()))
coinList = []
count = 0

for i in range(N):
    num = int(input())
    if num < K:
        coinList.append(num)
    else:
        break

for i in range(len(coinList),0,-1):
    count += K // coinList[i - 1]
    K -= (K // coinList[i - 1]) * coinList[i - 1]
    if K == 0:
        break

print(count)
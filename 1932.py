N = int(input())
dp =[]

for i in range(N):
    dp.append(list(map(int,input().split())))
for i in range(N-1):
    for j in range(len(dp[i+1])):
        if (j == 0):
            dp[i + 1][j] = dp[i][j] + dp[i + 1][j]
        elif (j == len(dp[i+1]) - 1):
            dp[i + 1][-1] = dp[i][-1] + dp[i + 1][-1]
        else:
            dp[i + 1][j] = max(dp[i][j - 1] + dp[i + 1][j], dp[i][j] + dp[i + 1][j])

print(max(dp[-1]))
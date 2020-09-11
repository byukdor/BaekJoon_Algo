N = int(input())
salary = [0] * (N + 1)
maximum = 0

for i in range(1, N + 1):
    day, money = list(map(int,input().split()))
    maximum = max(maximum,salary[i - 1])

    if (i + day - 1) <= N :
        salary[i + day - 1] = max(salary[i + day - 1], maximum + money)


print(max(salary))
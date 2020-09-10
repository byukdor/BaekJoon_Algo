N = int(input())
b = list(map(int,input().split()))
temp = [0] * N
result = -1001

for i in range(N):
    temp[i] = max(temp[i-1] + b[i], b[i])
    result = max(result, temp[i])
        
print(result)
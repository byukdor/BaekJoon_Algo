x = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer = 0

for i in range(x):
    answer += max(A) * min(B)
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))

print(answer)




N = 10
answer = 0

for i in range(N):
    new = int(input())
    if abs(100 - answer - new) > abs(100 - answer):
        print(answer)
        break
    elif abs(100 - answer - new) == abs(100 - answer):
        answer += new
        print(answer)
        break
    else:
        answer += new
    if i == (N - 1):
        print(answer)
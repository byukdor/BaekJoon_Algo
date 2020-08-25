length = int(input())
score = list(map(int,input().split()))
maximum = max(score)

for i in range(length):
    score[i] = score[i] / maximum * 100

print(sum(score)/length)
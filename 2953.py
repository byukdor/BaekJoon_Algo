scores = []
for i in range(5):
    scores.append(sum(list(map(int,input().split()))))

answer = [str(scores.index(max(scores))+1), str(max(scores))]

print(" ".join(answer))
point = []
answerIndex = []

for i in range(8):
    point.append(int(input()))

for i in sorted(point)[3:8]:
    answerIndex.append(str(point.index(i)+1))

print(sum(sorted(point)[3:8]))
print(" ".join(sorted(answerIndex)))


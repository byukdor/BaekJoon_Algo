N = int(input())
rope = []
maximum = 0


for i in range(N):
    rope.append(int(input()))

rope.sort()

for i in range(N):
    maximum = max(maximum,rope[i] * (N - i))

print(maximum)
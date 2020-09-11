N = 9
height = []

for i in range(N):
    height.append(int(input()))

total = sum(height)
height.sort()
done = False

for i in range(N - 1):
    for j in range(i + 1, N):
        if total - height[i] - height[j] == 100:
            done = True
            height.remove(height[i])
            height.remove(height[j - 1])
            break
    if done:
        break

for i in height:
    print(i)
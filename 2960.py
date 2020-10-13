N, K = map(int,input().split())

count = 0
num_list = [1] * (N + 1)

for i in range(2,N+1):
    for j in range(i,N + 1, i):
        if num_list[j]:
            num_list[j] = 0
            count += 1
            if count == K:
                print(j)
                break
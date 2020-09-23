N = int(input())

for i in range(N):
    K = int(input())
    H = int(input())
    num_list = list(range(1,H+1))

    for j in range(K):
        for k in range(1,H):
            num_list[k] += num_list[k-1]
    print(num_list[-1])
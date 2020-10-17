N = list(map(int,list(input())))

if (N.count(0) == 0) | (sum(N) % 3) :
    print(-1)
else:
    N.sort(reverse=True)
    print("".join(map(str,N)))
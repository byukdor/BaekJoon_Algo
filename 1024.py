
N, L = list(map(int,input().split()))
sigma = int(L * ((L - 1) / 2))
answer = True

while ((N - sigma) / L) % 1 > 0:
    L += 1
    sigma = int(L * ((L - 1) / 2))
    if (sigma > N):
        print(-1)
        answer = False
        break

if answer:
    result = list(range((N - sigma) // L, (N - sigma) // L + L ))

    if (min(result) < 0) | (L > 100):
        print(-1)
    else:
        print(" ".join(map(str,result)))

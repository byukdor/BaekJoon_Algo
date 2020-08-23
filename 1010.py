X = int(input())

for _ in range(X):
    r, n = list(map(int,input().split()))
    lower = n - r
    
    fact_1 = 1
    fact_2 = 1

    while n > lower:
        fact_1 *= n
        n -= 1
    
    while r > 0 :
        fact_2 *= r
        r -= 1
    
    print(int(fact_1 / fact_2))



N = int(input())

for i in range(N):
    A,B = map(int,input().split())
    A,B = min(A,B), max(A,B)
    product = A * B

    while B:
        A = A % B
        A, B = B, A
    print( int(product / A))
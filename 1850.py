
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

A, B = list(map(int,input().split()))
A, B = [min(A,B), max(A,B)]

if B % A == 0:
    print("1" * A)
else:
    print("1" * gcd(A, B - A))
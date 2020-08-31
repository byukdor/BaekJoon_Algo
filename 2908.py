A, B = list(map(list,input().split()))
N = 3

A[0], A[2] = A[2], A[0]
B[0], B[2] = B[2], B[0]

print(max(int("".join(A)),int("".join(B))))
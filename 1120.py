A, B = list(input().split())

maximum = 0
count = 0

for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] == B[i+j]:
            count +=1
    if count > maximum:
        maximum = count

print(len(A) - maximum)
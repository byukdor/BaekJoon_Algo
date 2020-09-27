L, R = list(map(str,input().split()))

result = 0

if len(R) != len(L):
    print(0)
else:
    if R != L:
        for i in range(len(R)):
            if (R[i] == L[i]):
                if (R[i] == '8'):
                    result += 1
            else:
                break
        print(result)
    else:
        print(R.count("8"))

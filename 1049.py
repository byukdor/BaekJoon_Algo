N, M = map(int,input().split())
min_bundle = 999999
min_each = 999999

for i in range(M):
    bundle, each = map(int,input().split())
    min_bundle = min(min_bundle,bundle)
    min_each = min(min_each,each)

if min_each * 6 <= min_bundle:
    print(N * min_each )
else:
    if (min_each * (N % 6)) >= min_bundle:
        print(((N // 6) + 1) * min_bundle )
    else:
        print((N // 6) * min_bundle + (N % 6) * min_each)
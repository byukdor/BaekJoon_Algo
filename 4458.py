N = int(input())

for i in range(N):
    list_ = input().split()
    list_[0] = list_[0][0].upper() + list_[0][1:]
    print(" ".join(list_))
start = [1,2,3]

def swap(list_, first, second):
    list_[first], list_[second] = list_[second], list_[first]
    return(list_)

for i in range(int(input())):
    first, second = list(map(int,input().split()))
    swap(start, start.index(first), start.index(second))

print(start[0])
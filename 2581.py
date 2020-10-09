start = int(input())
end = int(input())

num_list = [1] * (end + 1)

for i in range(2,end+1):
    if num_list[i] == 1:
        num_list[i] = i
        for j in range(i+i, end + 1, i):
            num_list[j] = 0
    else:
        pass

num_list = [x for x in num_list[2:] if (x >= start) & (x != 0)]

if num_list:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)
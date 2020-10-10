N = int(input())
num_list = [1] * (10001)

for i in range(2,10001):
    if num_list[i] == 1:
        num_list[i] = i
        for j in range(i+i, 10001, i):
            num_list[j] = 0
    else:
        pass

num_list = [x for x in num_list[2:] if (x != 0)]

for i in range(N):
    end = int(input())
    
    if end/2 in num_list:
        print("{} {}".format(int(end/2),int(end/2)))
    else:
        num = 0
        for j in num_list:
            if j > end/2:
                break
            if (end - j) in num_list:
                num = max(num,j)
        print("{} {}".format(num, end-num))

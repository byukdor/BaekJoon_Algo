num_list = []
for i in range(10):
    N = int(input())
    if N % 42 in num_list:
        continue
    else:
        num_list.append(N % 42)

print(len(num_list))

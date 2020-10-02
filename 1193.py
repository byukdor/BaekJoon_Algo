i = int(input())

fib_list=[0]*(i+2)
fib_list[1]=1

for i in range(2,i+2):
    fib_list[i] = fib_list[i-1]+fib_list[i-2]

print(fib_list[i-1])
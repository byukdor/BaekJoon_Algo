N, K = list(map(int,input().split()))

def factorial(num, stop = None):
    answer = 1
    if stop != None:
        for i in range(num, stop, -1):
            answer *= i
    else:
        for i in range(num,0,-1):
            answer *= i
    return answer

print(int(factorial(N, N - K) / factorial(K)))
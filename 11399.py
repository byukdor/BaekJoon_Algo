N = int(input())

ppl = list(map(int,input().split()))
answer = 0
latest = 0

for i in sorted(ppl):
    answer += latest + i
    latest += i

print(answer)
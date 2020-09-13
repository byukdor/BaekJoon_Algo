from collections import deque

def dfs(graph,start):
    history = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in history:
            history.append(n)
            if n in graph:
                remainder = list(set(graph[n]) - set(history))
                remainder.sort(reverse = True)
                stack += remainder
    
    history = [str(x) for x in history]
    
    return " ".join(history)

def bfs(graph,start):
    history = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in history:
            history.append(n)
            if n in graph:
                remainder = list(set(graph[n]) - set(history))
                remainder.sort()
                queue += remainder
    
    history = [str(x) for x in history]
    
    return " ".join(history)



N, M, V = list(map(int,input().split()))
graph = {}

for i in range(M):
    first_node, second_node = list(map(int,input().split()))


    if first_node not in graph:
        graph[first_node] = [second_node]
    elif second_node not in graph[first_node]:
        graph[first_node].append(second_node)
    
    if second_node not in graph:
        graph[second_node] = [first_node]
    elif first_node not in graph[second_node]:
        graph[second_node].append(first_node)


print(dfs(graph, V))
print(bfs(graph, V))
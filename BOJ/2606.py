def dfs(v):
    global count
    visited[v] = True
    count += 1
    for i in range(1, num+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

num = int(input())

linenum = int(input())
graph = [[0] * (num+1) for _ in range(num+1)]

visited = [False] * (num+1)
count = -1

for _ in range(linenum):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(count)

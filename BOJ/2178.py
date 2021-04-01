def bfs(x,y):
    queue = []
    queue.append((x,y))
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
bfs(0,0)
print(graph[N-1][M-1])

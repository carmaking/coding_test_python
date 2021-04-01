from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global result
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))
                
    while queue:
        result += 1
        for _ in range(len(queue)):
          x, y = queue.popleft()
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
            
              if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
              if graph[nx][ny] == -1:
                continue
              elif graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
    for i in range(N):
      for j in range(M):
        if graph[i][j] == 0:
          return -1
    return result    

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
    
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = -1

print(bfs())

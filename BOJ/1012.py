import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    
    if not visited[x][y] and data[x][y] == 1:
        visited[x][y] = True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False
    
    
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    data = [[0] * M for _ in range(N)]
    for _ in range(K):
        b, a = map(int, input().split())
        data[a][b] = 1
    result = 0
    
    for i in range(N):
      for j in range(M):
        if dfs(i,j) == True:
          result += 1
    print(result)

N = int(input())

graph = []
for _ in range(N):
  graph.append(list(map(int,input())))

visited = [[False] * N for _ in range(N)]

number = 0
number_map = []

def dfs(x,y):
    global number
    
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        number += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0


for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            result += 1
            number_map.append(number)
            number = 0

print(result)
number_map.sort()
for i in number_map:
  print(i)

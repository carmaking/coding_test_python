#이해요망
N = int(input())

data = list(map(int, input().split()))

stack = []
answer = [-1] * N

for i in range(N):
  while stack and data[stack[-1]] < data[i]:
    answer[stack.pop()] = data[i]
  
  stack.append(i)

print(*answer)

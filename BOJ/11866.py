from collections import deque

N, K = map(int, input().split())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

print('<',end='')
while len(queue) != 1:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')
print(queue[0],end='')
print('>')

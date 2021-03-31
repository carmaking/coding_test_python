from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
N = int(input())

for i in range(N):
    input_data = input().split()
    if input_data[0] == 'push':
        queue.append(input_data[1])
    elif input_data[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif input_data[0] == 'size':
        print(len(queue))
    elif input_data[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif input_data[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif input_data[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        

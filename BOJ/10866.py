from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    input_data = input().split()
    
    if input_data[0] == 'push_front':
        queue.appendleft(input_data[1])
    elif input_data[0] == 'push_back':
        queue.append(input_data[1])
    elif input_data[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif input_data[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif input_data[0] == 'size':
        print(len(queue))
    elif input_data[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
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

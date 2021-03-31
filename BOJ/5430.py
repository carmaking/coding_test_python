from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
T = int(input())

for _ in range(T):
    error = 0
    p = input()
    n = int(input())
    queue = deque(input()[1:-2].split(','))
    direction = True
    if n == 0:
      queue = []
    for i in range(len(p)):
        if p[i] == 'R':
            direction = not direction
        elif p[i] == 'D':
            if queue:
              if direction:
                queue.popleft()
              else:
                queue.pop()
            else:
                print('error')
                error = 1
                break
    if direction == False:
      queue.reverse()
    if error == 0:
        print('[',end='')
        for i in range(len(queue)):
            print(queue[i],end='')
            if i != len(queue) - 1:
                print(',',end='')
        print(']')

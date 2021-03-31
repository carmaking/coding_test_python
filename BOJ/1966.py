import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    check = deque([0] * len(queue))
    check[M] = 1
    count = 0
    
    while queue:
        if queue[0] == max(queue):
            count += 1
            queue.popleft()
            x = check.popleft()
            if x == 1:
                break
        else:
            queue.append(queue.popleft())
            check.append(check.popleft())
            
    print(count)

from collections import deque

N, M = map(int, input().split())

number = deque([i for i in range(1, N+1)])
data = deque(map(int, input().split()))
count = 0

while 1:
    if data[0] == number[0]:
        data.popleft()
        number.popleft()
        if len(data) == 0:
          break
    else:
        index = number.index(data[0])
        if index < 1 + len(number) - index:
            number.append(number.popleft())
            count += 1
        else:
            number.appendleft(number.pop())
            count += 1
         
print(count)

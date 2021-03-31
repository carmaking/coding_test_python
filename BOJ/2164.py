from collections import deque

N = int(input())

card = deque()
for i in range(1,N+1):
    card.append(i)
    
mode = 0
while len(card) != 1:
    if mode == 0:
        card.popleft()
        mode = 1
    else:
        card.append(card.popleft())
        mode = 0

print(card[0])

N = int(input())

a = []

for _ in range(N):
    start, end = map(int, input().split())
    a.append([start, end])

a.sort(key = lambda a:a[0])
a.sort(key = lambda a:a[1])
    
last = 0
count = 0
for i, j in a:
    if i >= last:
        count += 1
        last = j
    
print(count)

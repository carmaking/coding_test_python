N = int(input())

data = list(map(int, input().split()))

data.sort()

time = 0
    
for i in range(1, N+1):
    time += sum(data[:i])    

print(time)

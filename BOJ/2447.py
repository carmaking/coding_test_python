def star(length, x, y):
    if length == 1:
        return
    
    nx1, nx2 = x + length // 3, x + 2 * length // 3
    ny1, ny2 = y + length // 3, y + 2 * length // 3
    
    for i in range(nx1, nx2):
        for j in range(ny1, ny2):
            data[i][j] = ' '
    star(length // 3, x, y)
    star(length // 3, nx1, y)
    star(length // 3, nx2, y)
    star(length // 3, x, ny1)
    star(length // 3, x, ny2)
    star(length // 3, nx1, ny2)
    star(length // 3, nx2, ny1)
    star(length // 3, nx2, ny2)

N = int(input())
    
data = [['*'] * N for _ in range(N)]
star(N,0,0)
for t in data:
    print(''.join(t))

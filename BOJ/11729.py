def hanoi(N, a, b, c):
    if N == 1:
        array.append([a, c])
    else:
      hanoi(N-1, a, c, b)
      array.append([a,c])
      hanoi(N-1, b, a, c)

N = int(input())    
array = []
hanoi(N, 1, 2, 3)

print(len(array))
for i in range(len(array)):
    for j in range(2):
        print(array[i][j], end=' ')
    print()

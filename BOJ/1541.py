data = input().split('-')

for i in range(len(data)):
    data[i] = data[i].split('+')

result = 0

for i in range(len(data[0])):
  result += int(data[0][i])

for i in range(1, len(data)):
  num = 0
  for j in range(0, len(data[i])):
    num += int(data[i][j])

  result -= num

print(result)

n = int(input())

data = []

for _ in range(n):
  data.append(int(input()))

stack = []
order = []
num = 1

for i in range(n):
  while num <= data[i]:
    stack.append(num)
    order.append('+')
    num += 1
  if stack[-1] == data[i]:
    stack.pop()
    order.append('-')

if stack:
  print('NO')
else:
  for i in range(len(order)):
    print(order[i])

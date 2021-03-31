T = int(input())

for _ in range(T):
    data = list(input())
    stack = []
    answer = 'YES'
    check = 0
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        
        elif data[i] == ')':
            if stack:
                stack.pop()
            else:
                answer = 'NO'
                check = 1
                break

    if check == 0 and len(stack) > 0:
      answer = 'NO'
    elif check == 0 and len(stack) == 0:
      pass
    print(answer)

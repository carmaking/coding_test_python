import sys
input = sys.stdin.readline

while 1:
    S = input().rstrip()
    if S == '.':
      break
    stack = []
    answer = 'yes'
    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
              answer = 'no'
              break
            if stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif i == ']':
            if not stack:
                answer = 'no'
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
    
    if len(stack) > 0:
      answer = 'no'
    print(answer)

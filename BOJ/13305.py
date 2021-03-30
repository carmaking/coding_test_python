N = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

result = 0
money = price[0]

for i in range(N-1):
    if price[i] < money:
        money = price[i]
    result += money * road[i]

print(result)

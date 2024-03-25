num = list(map(int, input().strip("[]").split(",")))


for i in range(1, len(num)):
    num[i] += num[i-1]

print(num)


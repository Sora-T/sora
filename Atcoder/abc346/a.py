n = int(input())

b = list(map(int, input().split()))


ans = []

for i in range(0, n-1):
    ans.append((b[i]*b[i+1]))


print(*ans)

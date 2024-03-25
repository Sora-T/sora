x = list(input())
xx = x[::-1]

n = len(x)
nn = len(xx)

for i in range(n):
    for j in range(nn):
        if x[i] == xx[j]:
            print("true")
        
        else:
            print("false")



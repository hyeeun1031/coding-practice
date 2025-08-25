n,m = map(int, input().split())

baskets = [0] * n

for _ in range(m):
    i,j,k = map(int, input().split())
    
    for index in range(i-1, j):
        baskets[index] = k

print(*baskets)
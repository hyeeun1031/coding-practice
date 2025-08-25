n,m = map(int, input().split())
baskets = [i for i in range(1, n+1)]

for _ in range(m):
    i,j = map(int, input().split())
    
    i -= 1
    j -= 1
    baskets[i], baskets[j] = baskets[j], baskets[i]
    
print(*baskets)
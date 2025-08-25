n,m = map(int, input().split())
baskets = [i for i in range(1, n+1)]

for _ in range(m):
    i,j = map(int, input().split())
    left, right = i-1, j-1
    
    while left < right:
        baskets[left], baskets[right] = baskets[right], baskets[left]
        left += 1
        right -= 1
        
print(*baskets)
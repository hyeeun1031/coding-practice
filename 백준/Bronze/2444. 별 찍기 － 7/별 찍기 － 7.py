n = int(input())

# 위쪽 삼각형 (1번째 줄부터 N번째 줄까지)
for i in range(1, n+1):
    spaces = " " * (n - i)
    stars = '*' * (2*i - 1)
    print(spaces + stars)
    
# 아래쪽 삼각형 (N+1번째 줄부터 2*N-1번째 줄까지)
for j in range(1, n):
    spaces = ' ' * j
    stars = '*' * (2 * (n-j) - 1)
    print(spaces + stars)
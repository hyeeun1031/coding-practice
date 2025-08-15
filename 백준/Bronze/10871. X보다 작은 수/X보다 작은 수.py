n, x = map(int, input().split())
a = list(map(int, input().split()))

for n in a:
    if n < x:
        print(n, end=' ')
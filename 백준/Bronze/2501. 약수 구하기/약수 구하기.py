n,k = map(int, input().split())

cnt = 0
for d in range(1, n+1):
    if n% d == 0:
        cnt += 1
        if cnt == k:
            print(d)
            break
else:
    print(0)
N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    result = []
    for j in range(M):
        result.append(A[i][j] + B[i][j])
    print(*result)
import sys

N = int(sys.stdin.readline().strip())

i = 2
while i * i <= N:
    while N % i == 0:
        print(i)
        N //= i
    i += 1

if N > 1:
    print(N)
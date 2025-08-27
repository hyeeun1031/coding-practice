import sys
input = sys.stdin.readline

T = int(input().strip())
coins = [25, 10, 5, 1]

for _ in range(T):
    c = int(input().strip())
    q = c // 25; c %= 25
    d = c // 10; c %= 10
    n = c // 5;  c %= 5
    p = c
    # 정확히 한 줄만, 불필요한 공백/빈줄 없이
    sys.stdout.write(f"{q} {d} {n} {p}\n")

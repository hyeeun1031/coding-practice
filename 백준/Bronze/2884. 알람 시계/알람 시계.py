H, M = map(int, input().split())
M -= 45  # 45분 빼기

if M < 0:         # 분이 음수가 되면
    M += 60       # 60분 더해서 보정
    H -= 1        # 한 시간 빼기
    if H < 0:     # 시간이 음수가 되면 전날로 돌아감
        H = 23

print(H, M)

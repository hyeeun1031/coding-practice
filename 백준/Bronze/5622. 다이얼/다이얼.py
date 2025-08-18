s = input().strip()

groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for ch in s:
    for i, g in enumerate(groups, start = 3):
        if ch in g:
            time += i
            break

print(time)
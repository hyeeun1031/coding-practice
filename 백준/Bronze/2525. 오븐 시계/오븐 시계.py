A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C
end_h = (total // 60) % 24
end_m = total % 60

print(end_h, end_m)
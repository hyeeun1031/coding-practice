# 1. 과목 개수 입력
n = int(input())

# 2. 점수 입력 (리스트)
scores = list(map(int, input().split()))

# 3. 최대값
m = max(scores)

# 4. 변환된 점수 합 계산
new_scores = []

for s in scores:
    new_score = (s / m) * 100
    new_scores.append(new_score)

# 5. 평균 계산
avg = sum(new_scores)/n

print(avg)
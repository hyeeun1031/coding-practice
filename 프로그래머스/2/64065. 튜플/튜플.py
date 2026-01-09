def solution(s):
    # 1. 바깥 {{ }} 제거
    s = s[2:-2]

    # 2. 집합 단위로 분리
    sets = s.split("},{")

    # 3. 각 집합을 리스트로 변환
    parsed = [list(map(int, x.split(','))) for x in sets]

    # 4. 길이 기준 정렬
    parsed.sort(key=len)

    # 5. 튜플 복원
    answer = []
    used = set()

    for group in parsed:
        for num in group:
            if num not in used:
                answer.append(num)
                used.add(num)

    return answer

def solution(s):
    last_seen = {}   # 각 문자 마지막 등장 인덱스 저장용
    answer = []

    for i, ch in enumerate(s):
        if ch in last_seen:
            # 현재 위치(i)에서 이전 등장 위치(last_seen[ch])까지의 거리 계산
            answer.append(i - last_seen[ch])
        else:
            # 처음 등장한 문자면 -1
            answer.append(-1)
        # 현재 문자의 마지막 등장 위치 갱신
        last_seen[ch] = i

    return answer

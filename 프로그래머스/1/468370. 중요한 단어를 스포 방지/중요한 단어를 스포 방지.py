def solution(message, spoiler_ranges):
    n = len(message)
    m = len(spoiler_ranges)

    # 각 문자에 어떤 spoiler 구간이 적용됐는지 기록
    cover = [-1] * n
    for idx, (s, e) in enumerate(spoiler_ranges):
        for i in range(s, e + 1):
            cover[i] = idx

    # plain_words: 스포가 전혀 없는 위치에서 등장한 단어들
    plain_words = set()

    # revealed_at[i]: i번째 클릭 때 완전히 공개되는 단어들(왼쪽->오른쪽 순서 유지)
    revealed_at = [[] for _ in range(m)]

    # message를 단어 단위로 파싱
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue

        start = i
        while i < n and message[i] != ' ':
            i += 1
        end = i - 1

        word = message[start:i]

        # 이 단어가 어떤 spoiler 구간에 걸쳐 있는지 확인
        last_idx = -1
        for p in range(start, end + 1):
            if cover[p] != -1:
                last_idx = max(last_idx, cover[p])

        if last_idx == -1:
            # 한 번도 스포 구간에 안 걸린 단어
            plain_words.add(word)
        else:
            # 마지막 spoiler 구간이 클릭될 때 완전히 공개됨
            revealed_at[last_idx].append(word)

    # 클릭 순서대로 중요한 단어 판별
    seen_spoiler_words = set()
    answer = 0

    for idx in range(m):
        for word in revealed_at[idx]:
            if word not in plain_words and word not in seen_spoiler_words:
                answer += 1
            # 공개된 스포 단어는 중요 여부와 무관하게 이후 중복 체크 대상
            seen_spoiler_words.add(word)

    return answer
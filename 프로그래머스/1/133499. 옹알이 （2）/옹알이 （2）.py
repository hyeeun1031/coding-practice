def solution(babbling):
    allowed = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for word in babbling:
        i = 0
        prev = ""   # 직전에 쓴 음절(연속 금지용)
        ok = True

        while i < len(word):
            matched = False
            for syl in allowed:
                if word.startswith(syl, i) and syl != prev:
                    i += len(syl)
                    prev = syl
                    matched = True
                    break
            if not matched:
                ok = False
                break

        if ok and i == len(word):
            cnt += 1

    return cnt

def solution(s, skip, index):
    from string import ascii_lowercase

    # 1. 알파벳 리스트 생성
    alphabet = list(ascii_lowercase)

    # 2. skip 문자 제거
    for ch in skip:
        alphabet.remove(ch)

    # 3. 변환 결과 저장
    result = ""

    # 4. 변환 로직
    for ch in s:
        now_idx = alphabet.index(ch)
        new_idx = (now_idx + index) % len(alphabet)
        result += alphabet[new_idx]

    return result

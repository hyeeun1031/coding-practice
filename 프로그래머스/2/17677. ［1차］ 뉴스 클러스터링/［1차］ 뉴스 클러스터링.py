from collections import Counter

def make_multiset(s: str) -> Counter:
    s = s.lower()
    pairs = []
    for i in range(len(s) - 1):
        p = s[i:i+2]
        # 두 글자 모두 알파벳인지 확인
        if p[0].isalpha() and p[1].isalpha():
            pairs.append(p)
    return Counter(pairs)

def solution(str1: str, str2: str) -> int:
    c1 = make_multiset(str1)
    c2 = make_multiset(str2)

    # 둘 다 공집합이면 1로 정의
    if not c1 and not c2:
        return 65536

    # 다중집합 교집합/합집합 크기
    inter = sum((c1 & c2).values())   # Counter 교집합: min
    union = sum((c1 | c2).values())   # Counter 합집합: max

    return int((inter / union) * 65536)

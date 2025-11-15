from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sizes = sorted(count.values(), reverse=True)

    kinds = 0
    total = 0

    for c in sizes:
        total += c
        kinds += 1
        if total >= k:
            return kinds

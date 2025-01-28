from functools import reduce

def solution(numbers, target):

    # 가능한 모든 합을 추적하는 리스트
    sums = [0]

    for num in numbers:
        # 현재까지의 모든 합에 +num과 -num을 적용
        sums = [s + num for s in sums] + [s - num for s in sums]

    # 최종 합 중 target과 같은 경우의 수를 카운트
    return sums.count(target)
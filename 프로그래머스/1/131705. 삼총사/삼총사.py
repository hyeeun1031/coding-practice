from itertools import combinations

def solution(number):
    count = 0
    for trio in combinations(number, 3):  # 3명씩 조합
        if sum(trio) == 0:               # 합이 0이면 삼총사
            count += 1
    return count

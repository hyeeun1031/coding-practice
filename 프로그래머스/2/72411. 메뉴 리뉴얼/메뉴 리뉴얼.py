from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        for order in orders:
            # 각 주문 내 문자들을 알파벳 순으로 정렬
            sorted_order = sorted(order)
            # c개짜리 조합을 생성하여 리스트에 추가
            temp.extend(combinations(sorted_order, c))
        
        # 각 조합의 등장 횟수 카운팅
        counter = Counter(temp)
        
        # 2번 이상 주문된 조합 중 최다 주문된 조합 찾기
        if counter and max(counter.values()) >= 2:
            max_val = max(counter.values())
            for menu, count in counter.items():
                if count == max_val:
                    answer.append("".join(menu))
                    
    # 최종 코스 메뉴들을 사전 순(알파벳 오름차순)으로 정렬
    return sorted(answer)
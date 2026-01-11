import heapq

def solution(n, works):
    # 총 작업량이 n 이하라면 모두 처리 가능
    if sum(works) <= n:
        return 0

    # 최대 힙을 만들기 위해 음수로 변환
    heap = [-w for w in works]
    heapq.heapify(heap)

    for _ in range(n):
        largest = -heapq.heappop(heap)
        if largest == 0:
            break
        largest -= 1
        heapq.heappush(heap, -largest)

    # 야근 피로도 계산
    return sum(x * x for x in map(lambda x: -x, heap))

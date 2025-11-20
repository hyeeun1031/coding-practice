import heapq

def time_to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    # 1. 종료시간 + 청소시간(10분) 반영
    times = []
    for start, end in book_time:
        s = time_to_min(start)
        e = time_to_min(end) + 10
        times.append((s, e))
    
    # 2. 시작 시각 기준 정렬
    times.sort()
    
    # 3. 최소 힙 사용
    heap = []
    
    for s, e in times:
        # 힙이 비어있지 않고, 가장 빠른 종료 시각 <= 현재 시작 시각 → 방 재사용 가능
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        
        # 현재 예약의 종료시간(청소 포함) 삽입
        heapq.heappush(heap, e)
    
    return len(heap)

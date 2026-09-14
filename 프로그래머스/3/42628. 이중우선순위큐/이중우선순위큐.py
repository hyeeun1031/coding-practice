import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    count = {}

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            count[value] = count.get(value, 0) + 1

        elif command == "D":
            if not count:
                continue

            if value == 1:
                # 최댓값 삭제
                while max_heap and count.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    num = -heapq.heappop(max_heap)
                    count[num] -= 1

                    if count[num] == 0:
                        del count[num]

            else:
                # 최솟값 삭제
                while min_heap and count.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)

                if min_heap:
                    num = heapq.heappop(min_heap)
                    count[num] -= 1

                    if count[num] == 0:
                        del count[num]

    # 삭제된 값들을 힙에서 제거
    while min_heap and count.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    while max_heap and count.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    if not count:
        return [0, 0]

    return [-max_heap[0], min_heap[0]]
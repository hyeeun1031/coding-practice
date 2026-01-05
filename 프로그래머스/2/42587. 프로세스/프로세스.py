from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        current_priority, current_idx = queue.popleft()

        # 현재 프로세스보다 높은 우선순위가 큐에 존재하는지 확인
        if any(current_priority < p for p, _ in queue):
            queue.append((current_priority, current_idx))
        else:
            order += 1
            if current_idx == location:
                return order

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 상태 (0은 빈 칸)
    total_weight = 0                     # 다리 위 트럭들의 총 무게
    time = 0
    trucks = deque(truck_weights)

    while trucks:
        # 다리 맨 앞 트럭(혹은 빈 칸)을 내림
        total_weight -= bridge.popleft()
        time += 1

        # 다음 트럭을 올릴 수 있는지 확인
        if total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)  # 못 올리면 빈 칸으로 채움

    # 마지막 트럭이 다리를 완전히 건널 때까지 대기
    time += bridge_length

    return time
def solution(k, dungeons):
    max_count = 0      # 탐험 가능한 최대 던전 수
    n = len(dungeons)
    visited = [False] * n

    def dfs(fatigue, count):
        nonlocal max_count
        # 지금까지 돈 던전 수로 최대값 갱신
        if count > max_count:
            max_count = count

        # 현재 상태에서 갈 수 있는 다음 던전을 모두 시도
        for i in range(n):
            need, cost = dungeons[i]

            # 아직 안 돌았고, 피로도가 최소 필요 피로도 이상이면
            if not visited[i] and fatigue >= need:
                visited[i] = True
                dfs(fatigue - cost, count + 1)  # 다음 상태로 진행
                visited[i] = False              # 백트래킹 (원상 복구)

    # 시작: 초기 피로도 k, 탐험한 던전 수 0
    dfs(k, 0)

    return max_count

def solution(n, computers):
    visited = [False] * n  # 방문 여부를 기록할 리스트
    network_count = 0

    def dfs(node):
        visited[node] = True  # 현재 노드 방문 처리
        for neighbor in range(n):
            # 자기 자신이 아니고, 연결되어 있으며, 아직 방문하지 않은 경우
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs(i)  # 방문하지 않은 노드에서 DFS 시작
            network_count += 1  # 새로운 네트워크 발견

    return network_count
def solution(n, wires):
    answer = n

    # 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 특정 전선을 끊었을 때 한쪽 네트워크의 송전탑 개수
    def dfs(start, cut_a, cut_b):
        visited = [False] * (n + 1)
        stack = [start]
        visited[start] = True
        count = 0

        while stack:
            node = stack.pop()
            count += 1

            for next_node in graph[node]:
                # 끊은 전선은 건너뛰기
                if (node == cut_a and next_node == cut_b) or \
                   (node == cut_b and next_node == cut_a):
                    continue

                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)

        return count

    # 모든 전선을 하나씩 끊어보기
    for a, b in wires:
        count = dfs(a, a, b)

        other = n - count
        diff = abs(count - other)

        answer = min(answer, diff)

    return answer
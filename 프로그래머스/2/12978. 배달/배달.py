import heapq

def solution(N, road, K):
    # 인접 리스트
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))  # 양방향
    
    # 최단 거리 배열
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[1] = 0
    
    # 우선순위 큐
    pq = [(0, 1)]  # (거리, 마을)
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        # 이미 더 짧은 거리로 처리된 경우
        if dist > distance[now]:
            continue
        
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    # K 이하인 마을의 개수
    return sum(d <= K for d in distance)
def solution(triangle):
    # 맨 아래부터 시작
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]
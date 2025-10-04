def solution(rank, attendance):
    # 학생 번호, 등수, 참석 여부 묶어서 리스트 생성
    students = [(i, rank[i], attendance[i]) for i in range(len(rank))]
    
    # 참석 가능한 학생만 필터링
    available = [s for s in students if s[2]]
    
    # 등수 기준으로 정렬
    available.sort(key=lambda x: x[1])
    
    # 상위 3명 번호 추출
    a, b, c = available[0][0], available[1][0], available[2][0]
    
    # 문제에서 제시한 계산식 적용
    return 10000 * a + 100 * b + c

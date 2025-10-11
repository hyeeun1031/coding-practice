def solution(numlist, n):
    # 거리와 값 기준으로 정렬하는 함수 정의
    def 기준(x):
        거리 = abs(x - n)   # n과의 거리
        return (거리, -x)   # 거리 우선, 같으면 큰 수 먼저

    # 기준 함수에 따라 정렬
    numlist.sort(key=기준)
    return numlist

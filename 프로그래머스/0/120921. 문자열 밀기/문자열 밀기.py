def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        # 오른쪽으로 한 칸 밀기: 마지막 글자를 앞으로
        A = A[-1] + A[:-1]
    return -1

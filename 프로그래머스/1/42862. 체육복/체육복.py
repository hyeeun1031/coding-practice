def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 1. 본인도 잃어버리고 여벌도 있는 학생 제거
    common = lost_set & reserve_set
    lost_set -= common
    reserve_set -= common

    # 2. 체육복 빌려주기
    answer = n
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            answer -= 1

    return answer

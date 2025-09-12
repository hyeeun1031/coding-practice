def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):  # n씩 건너뛰면서 반복
        result.append(num_list[i:i+n])    # i부터 i+n까지 잘라서 추가
    return result

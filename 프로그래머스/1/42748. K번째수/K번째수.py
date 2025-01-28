def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = array[i-1:j]
        sorted_sliced = sorted(sliced)
        answer.append(sorted_sliced[k-1])
    return answer

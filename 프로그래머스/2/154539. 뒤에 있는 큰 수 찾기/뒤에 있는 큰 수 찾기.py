def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []  # 인덱스를 저장

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)

    return answer

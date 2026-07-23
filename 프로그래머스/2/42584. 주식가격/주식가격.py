def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 가격이 아직 안 떨어진 인덱스들을 저장

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 스택에 남아있는 것들은 끝까지 가격이 안 떨어진 것
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer
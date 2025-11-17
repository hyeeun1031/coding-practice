def solution(ingredient):
    stack = []
    count = 0

    for x in ingredient:
        stack.append(x)

        # 스택 마지막 4개가 1-2-3-1인지 검사
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                # 햄버거 완성 → 4개 제거
                del stack[-4:]
                count += 1

    return count

def solution(n, k):
    answer = []
    people = list(range(1, n + 1))

    k -= 1  # 0-based index

    for i in range(n, 0, -1):
        factorial = 1

        for j in range(1, i):
            factorial *= j

        index = k // factorial
        k %= factorial

        answer.append(people.pop(index))

    return answer
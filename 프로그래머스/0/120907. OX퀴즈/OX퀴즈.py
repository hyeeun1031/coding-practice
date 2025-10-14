def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, z = q.split()
        if op == '+':
            result = int(x) + int(y)
        else:
            result = int(x) - int(y)
        
        if result == int(z):
            answer.append("O")
        else:
            answer.append("X")
    return answer

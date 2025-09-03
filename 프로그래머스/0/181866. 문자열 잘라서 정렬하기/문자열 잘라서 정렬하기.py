def solution(myString):
    parts = myString.split("x")
    answer = []
    for p in parts:
        if p != "":
            answer.append(p)
    return sorted(answer)
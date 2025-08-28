def solution(myString):
    parts = myString.split("x")
    answer = []
    
    for s in parts:
        answer.append(len(s))
        
    return answer
def solution(arr):
    answer = []
    
    for num in arr:
        if not answer: # 스택이 비어있으면
            answer.append(num)
        elif answer[-1] == num: # 스택의 마지막 원소와 현재 원소가 같으면 pop
            answer.pop()
        else:
            answer.append(num)
    return answer if answer else[-1]
def solution(intStrs, k, s, l):
    answer = []
    
    for x in intStrs:
        num = int(x[s:s+l])   # 부분 문자열에서 정수
        if num > k:
            answer.append(num)
            
    return answer
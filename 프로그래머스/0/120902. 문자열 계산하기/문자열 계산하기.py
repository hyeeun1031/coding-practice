def solution(my_string):
    tokens = my_string.split()  
    result = int(tokens[0])     
    
    for i in range(1, len(tokens), 2):  # 연산자는 홀수 위치
        op = tokens[i]          # '+' 또는 '-'
        num = int(tokens[i+1])  # 숫자
        
        if op == '+':
            result += num
        else:  # op == '-'
            result -= num
    
    return result
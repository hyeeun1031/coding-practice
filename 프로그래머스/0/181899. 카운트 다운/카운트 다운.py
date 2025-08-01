def solution(start_num, end_num):
    answer = []
    
    for i in range(start_num, end_num-1, -1):
        answer.append(i)
    # start_num부터 end_num까지 1씩 감소하면서 숫자를 하나씩 꺼낸다
    # 파이썬의 range(start, end, step)에서 step을 -1로 주면 감소한다
    # end_num도 포함해야 하므로 end_num - 1까지가 아니라 end_num까지 반복
    
    return answer
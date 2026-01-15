def solution(wallet, bill):
    answer = 0
    
    # 항상 (작은 값, 큰 값) 기준으로 비교
    wallet.sort()
    bill.sort()
    
    # 지폐가 지갑에 안 들어가는 동안 반복
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        # 긴 쪽을 반으로 접기
        if bill[1] >= bill[0]:
            bill[1] //= 2
        else:
            bill[0] //= 2
        
        bill.sort()
        answer += 1
    
    return answer

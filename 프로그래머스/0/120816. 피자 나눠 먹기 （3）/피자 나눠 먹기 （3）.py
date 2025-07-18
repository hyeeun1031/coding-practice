def solution(slice, n):
    q = n //slice # 필요한 피자 조각 수를 피자 한 판의 조각 수로 나눈 몫
    r = n % slice # 나머지 계산
    
    if r > 0: # 나머지가 0보다 크다면 (모든 사람이 피자를 받지 못했다면)
        answer = q + 1 # 몫에 1을 더해 한 판 추가 주문
    else: # 나머지가 0이라면
        answer = q # 몫 만큼의 피자 주문
    return answer
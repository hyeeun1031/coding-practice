def solution(my_string, n):
    answer = '' 
    for i in range(n): # 0부터 n-1까지 반복
        answer += my_string[i] # i번째 글자를 결과에 붙임
    return answer
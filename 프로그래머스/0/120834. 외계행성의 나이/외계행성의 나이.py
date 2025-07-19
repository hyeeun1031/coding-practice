def solution(age):
    answer = ''
    for digit in str(age): # 나이를 문자열로 변환
        number = int(digit) # 숫자를 정수형으로 변환
        
        letter = chr(ord('a') + number) # 숫자를 알파벳으로 바꾸기 위해 아스키 코드 변환
        
        answer += letter
        
    return answer
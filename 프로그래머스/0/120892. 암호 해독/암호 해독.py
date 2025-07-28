def solution(cipher, code):
    answer = ''

    index = 0
    while index < len(cipher):
        if (index+1) % code == 0:
            answer += cipher[index]
        index += 1
    
    return answer
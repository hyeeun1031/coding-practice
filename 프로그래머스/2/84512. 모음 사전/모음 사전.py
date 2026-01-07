def solution(word):
    weights = [781, 156, 31, 6, 1]
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    answer = 0
    for i, ch in enumerate(word):
        answer += vowels.index(ch) * weights[i]
        answer += 1
    
    return answer

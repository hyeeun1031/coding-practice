def solution(s):
    def is_valid(brackets):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        
        for ch in brackets:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
        
        return not stack

    answer = 0
    n = len(s)
    
    for x in range(n):
        rotated = s[x:] + s[:x]
        if is_valid(rotated):
            answer += 1
    
    return answer

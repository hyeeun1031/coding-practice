from functools import cmp_to_key

def solution(numbers):
    strs = list(map(str, numbers))
    
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    strs.sort(key=cmp_to_key(compare))
    result = ''.join(strs)
    
    return '0' if result[0] == '0' else result
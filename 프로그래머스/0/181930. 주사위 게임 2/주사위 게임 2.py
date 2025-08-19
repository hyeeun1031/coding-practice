def solution(a:int, b:int, c:int) -> int:
    s1 = a+b+c
    s2 = a*a + b*b + c*c
    s3 = a*a*a + b*b*b + c*c*c
    
    kinds = len({a,b,c})
    
    if kinds == 1: # 세 숫자 모두 같음
        return s1*s2*s3
    elif kinds == 2: # 두 숫자만 같음
        return s1*s2
    else: # 모두 다름
        return s1
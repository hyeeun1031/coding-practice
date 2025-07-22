def factorial(n): # 1부터 n까지 곱해서 팩토리얼 값을 구하는 함수
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def solution(balls,share): # 조합 :  n! / (r! * (n-r)!)
    top = factorial(balls) # 분자 : balls!
    bottom = factorial(share) * factorial(balls - share) # 분모 share! * (balls-share)!
    return top // bottom
    
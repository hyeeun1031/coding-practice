def solution(number, n, m):
    n_multi = (number % n) == 0
    m_multi = (number % m) == 0
    
    if n_multi and m_multi:
        return 1
    else:
        return 0
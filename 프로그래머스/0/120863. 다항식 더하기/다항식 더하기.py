def solution(polynomial):
    terms = polynomial.split(" + ")
    x_sum = 0
    const_sum = 0
    
    for term in terms:
        if 'x' in term:
            coeff = term.replace('x', '')
            x_sum += int(coeff) if coeff else 1
        else:
            const_sum += int(term)
    
    # 출력 조합
    if x_sum and const_sum:
        return f"{x_sum}x + {const_sum}" if x_sum > 1 else f"x + {const_sum}"
    elif x_sum:
        return f"{x_sum}x" if x_sum > 1 else "x"
    else:
        return str(const_sum)

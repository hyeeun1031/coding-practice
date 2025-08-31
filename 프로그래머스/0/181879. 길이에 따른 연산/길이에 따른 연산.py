def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        prod = 1
        for x in num_list:
            prod *= x
        return prod
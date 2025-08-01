def solution(num_list):
    total_product = 1
    total_sum = 0
    
    for n in num_list:
        total_product *= n
        total_sum += n
    
    if total_product < total_sum ** 2:
        return 1
    else:
        return 0
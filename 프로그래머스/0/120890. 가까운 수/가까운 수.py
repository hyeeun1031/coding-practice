def solution(array, n):
    closest = array[0]
    
    for num in array:
        if abs(num-n) < abs(closest-n):
            closest = num
        elif abs(num-n) == abs(closest-n) and num < closest:
            closest = num
    return closest
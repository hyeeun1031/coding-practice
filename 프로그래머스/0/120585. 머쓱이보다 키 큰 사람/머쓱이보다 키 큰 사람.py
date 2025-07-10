def solution(array, height):
    count = 0
    
    for n in array:
        if n > height:
            count += 1
    
    return count
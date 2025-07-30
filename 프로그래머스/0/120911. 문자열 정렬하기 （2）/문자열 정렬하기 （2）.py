def solution(my_string):
    my_string = my_string.lower()
    
    sorted_string = ''.join(sorted(my_string))
    
    return sorted_string
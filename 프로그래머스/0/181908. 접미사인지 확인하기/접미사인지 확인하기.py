def solution(my_string, is_suffix):
    len_my = len(my_string)
    len_suf = len(is_suffix)
    
    if len_suf > len_my:
        return 0
    
    end_of_my_string = my_string[len_my - len_suf:]
    
    if end_of_my_string == is_suffix:
        return 1
    else:
        return 0
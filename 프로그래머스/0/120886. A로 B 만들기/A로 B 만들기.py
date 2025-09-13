def solution(before, after):
    before_list = list(before)
    after_list = list(after)
    
    before_list.sort()
    after_list.sort()
    
    if before_list == after_list:
        return 1
    else:
        return 0
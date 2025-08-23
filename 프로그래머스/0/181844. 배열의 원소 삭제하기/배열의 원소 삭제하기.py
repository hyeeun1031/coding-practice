def solution(arr, delete_list):
    
    result = []
    
    for x in arr:
        if x not in delete_list:
            result.append(x)
    
    return result
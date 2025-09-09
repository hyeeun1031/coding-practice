def solution(my_string, indices):
    remove_set = set(indices)
    answer = ""
    
    for i,ch in enumerate(my_string):
        if i not in remove_set:
            answer += ch
    return answer
def solution(my_string, queries):
    arr = list(my_string)
    
    for s, e in queries:
        while s<e:
            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp
            
            s += 1
            e -= 1
    return "".join(arr)
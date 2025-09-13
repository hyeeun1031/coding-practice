def solution(myStr):
    temp = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    
    parts = temp.split()
    
    if not parts:
        return ["EMPTY"]
    return parts
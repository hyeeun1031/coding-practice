def solution(myString, pat):
    swapped = ""
    
    for char in myString:
        if char == "A":
            swapped += "B"
        else:
            swapped += "A"
            
    if pat in swapped:
        return 1
    else:
        return 0
def solution(s):
    tokens = s.split()
    numbers = []
    
    for t in tokens:
        if t == "Z":
            numbers.pop()
        else:
            numbers.append(int(t))
            
    return sum(numbers)
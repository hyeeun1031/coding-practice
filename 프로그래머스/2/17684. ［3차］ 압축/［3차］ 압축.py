def solution(msg):
    dictionary = {chr(65+i): i+1 for i in range(26)}
    next_code = 27
    result = []
    w = ""
    for c in msg:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result
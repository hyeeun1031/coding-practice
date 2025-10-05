def solution(t, p):
    len_p = len(p)
    num_p = int(p)
    count = 0

    for i in range(len(t) - len_p + 1):
        substring = int(t[i:i + len_p])
        if substring <= num_p:
            count += 1
    return count

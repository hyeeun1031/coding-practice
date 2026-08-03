import re

def solution(files):
    parsed = []
    for f in files:
        m = re.match(r'^([^\d]+)(\d{1,5})(.*)$', f)
        head, number, tail = m.group(1), m.group(2), m.group(3)
        parsed.append((head.lower(), int(number), f))
    
    parsed.sort(key=lambda x: (x[0], x[1]))
    return [x[2] for x in parsed]
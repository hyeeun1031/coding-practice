def solution(arr):
    x = 0
    cur = list(arr)
    while True:
        changed = False
        new = []
        for v in cur:
            if v >= 50 and v % 2 == 0:
                nv = v // 2
            elif v < 50 and v % 2 == 1:
                nv = v * 2 + 1
            else:
                nv = v
            if nv != v:
                changed = True
            new.append(nv)
        if not changed:
            return x
        cur = new
        x += 1
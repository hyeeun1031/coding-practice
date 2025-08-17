t = int(input().strip())

for _ in range(t):
    r,s = input().split()
    r = int(r)
    
    result = ""
    for ch in s:
        result += ch * r # 각 문자를 r번 반복
    print(result)
def solution(code):
    mode = 0          # 처음에는 mode가 0
    ret = ''          # 결과 문자열 초기화

    for idx in range(len(code)):  # 문자열을 앞에서부터 한 글자씩 확인
        if code[idx] == '1':      # 현재 글자가 '1'이면
            mode = 1 - mode       # mode를 0<->1로 바꿈
        else:
            if mode == 0 and idx % 2 == 0:   # mode 0에서는 짝수 인덱스만 추가
                ret += code[idx]
            elif mode == 1 and idx % 2 == 1: # mode 1에서는 홀수 인덱스만 추가
                ret += code[idx]

    return ret if ret else "EMPTY"  # 비어 있으면 "EMPTY" 반환

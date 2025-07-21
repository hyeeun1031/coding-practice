def solution(my_string):
    total = 0  # 숫자들의 합을 저장할 변수

    for ch in my_string:  # 문자열에 있는 문자 하나씩 꺼내기
        if ch.isdigit():  # 만약 그 문자가 숫자라면
            total += int(ch)  # 숫자로 바꿔서 total에 더하기

    return total  # 최종 합을 반환
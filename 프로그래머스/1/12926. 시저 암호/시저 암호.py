def solution(s, n):
    result = ''
    for ch in s:
        if ch == ' ':  # 공백은 그대로
            result += ' '
        elif 'A' <= ch <= 'Z':  # 대문자일 경우
            result += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':  # 소문자일 경우
            result += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
    return result

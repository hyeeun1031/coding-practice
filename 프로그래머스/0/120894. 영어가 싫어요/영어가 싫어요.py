def solution(numbers):
    # 영어 숫자 단어와 실제 숫자의 매핑
    num_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # numbers 문자열에서 각 단어를 숫자로 치환
    for word, digit in num_map.items():
        numbers = numbers.replace(word, digit)

    # 최종적으로 정수로 변환
    return int(numbers)

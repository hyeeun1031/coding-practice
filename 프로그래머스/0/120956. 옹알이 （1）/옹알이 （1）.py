def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word
        # 가능한 단어를 공백으로 치환
        for p in possible:
            temp = temp.replace(p, " ")
        # 모든 발음 제거 후 남은 글자에 알파벳이 없으면 발음 가능
        # strip()은 공백 제거, isalpha()로 문자 남았는지 확인
        if temp.strip() == "":
            count += 1

    return count

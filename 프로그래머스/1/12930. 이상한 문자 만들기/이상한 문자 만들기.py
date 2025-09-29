def solution(s):
    words = s.split(" ")  # 공백 기준 단어 분리
    result = []
    
    for word in words:
        new_word = ""
        for i, ch in enumerate(word):
            if i % 2 == 0:
                new_word += ch.upper()
            else:
                new_word += ch.lower()
        result.append(new_word)
    
    return " ".join(result)

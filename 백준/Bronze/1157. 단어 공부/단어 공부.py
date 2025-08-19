word = input().strip()

# 알파벳 빈도 계산 (대소문자 구분 없이)
count = {}
for char in word:
    char_upper = char.upper()
    if char_upper in count:
        count[char_upper] += 1
    else:
        count[char_upper] = 1
        
# 최대 빈도 찾기
max_count = max(count.values())

# 최대 빈도를 가진 알파벳들 찾기
max_chars = []
for char, freq in count.items():
    if freq == max_count:
        max_chars.append(char)
        
# 결과 출력
if len(max_chars) == 1:
    print(max_chars[0])
else:
    print("?")
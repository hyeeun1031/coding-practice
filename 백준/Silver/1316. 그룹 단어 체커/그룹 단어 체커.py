def is_group_word(word):
    seen = set()
    prev_char = ''
    
    for char in word:
        if char != prev_char and char in seen:
            return False
        
        seen.add(char)
        prev_char = char
    
    return True

n = int(input())
group_word_count = 0

for _ in range(n):
    word = input().strip()
    if is_group_word(word):
        group_word_count += 1

print(group_word_count)
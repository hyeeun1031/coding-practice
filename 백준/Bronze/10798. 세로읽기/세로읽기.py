words = [input().strip() for _ in range(5)]

max_len = max(len(word) for word in words)

result = []

for col in range(max_len):
    for row in range(5):
        if col < len(words[row]):
            result.append(words[row][col])
            
print("".join(result))
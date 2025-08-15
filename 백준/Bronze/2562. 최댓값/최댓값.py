numbers = [int(input()) for _ in range(9)]

max_value = max(numbers)

position = numbers.index(max_value) + 1

print(max_value)
print(position)
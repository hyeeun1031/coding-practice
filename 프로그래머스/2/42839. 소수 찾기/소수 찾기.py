from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solution(numbers):
    candidates = set()
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            candidates.add(num)
    
    return sum(1 for num in candidates if is_prime(num))
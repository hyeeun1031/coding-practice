remainderset = set()

for _ in range(10):
    n = int(input())
    remainder = n % 42
    remainderset.add(remainder)
    
print(len(remainderset))
all = set(range(1, 31))

submitted = set()
for _ in range(28):
    n = int(input())
    submitted.add(n)
    
missing = list(all - submitted)

missing.sort()

print(missing[0])
print(missing[1])
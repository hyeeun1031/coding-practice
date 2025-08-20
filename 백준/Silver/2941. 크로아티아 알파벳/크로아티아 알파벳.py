word = input().strip()

c_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in c_alphabets:
    word = word.replace(a, '*')
    
print(len(word))
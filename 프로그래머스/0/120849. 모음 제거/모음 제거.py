def solution(my_string):
    vowels = 'aeiou'
    for v in vowels:
        my_string = my_string.replace(v, '')
    return my_string
def solution(my_string, num1, num2):
    char_list = list(my_string)
    
    temp = char_list[num1]
    char_list[num1] = char_list[num2]
    char_list[num2] = temp
    
    result = ''.join(char_list)
    
    return result
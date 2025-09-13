def solution(phone_number):
    length = len(phone_number)
    hidden = "*" * (length-4)
    visible = phone_number[-4:]
    
    return hidden + visible
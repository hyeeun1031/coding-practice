def solution(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    total = num1 + num2
    
    return bin(total)[2:]
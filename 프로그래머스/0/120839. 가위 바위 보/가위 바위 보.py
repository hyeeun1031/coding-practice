def solution(rsp):
    win_map = {'2' : '0', # 가위를 이기려면 바위
               '0' : '5', # 바위를 이기려면 보
               '5' : '2' # 보를 이기려면 가위
    }
    
    result = ""
    
    for move in rsp: # 입력 문자열의 가위바위보 확인
        result += win_map[move] # 이기는 손을 result에 더함
        
    return result
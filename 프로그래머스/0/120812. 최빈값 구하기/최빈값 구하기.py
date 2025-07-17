def solution(array):
    count_dict = {} # 각 숫자가 몇 번 나왔는지 세기 위해 딕셔너리 생성
    
    for n in array:
        if n in count_dict:
            count_dict[n] += 1 # 숫자가 이미 딕셔너리에 존재하면, 값(횟수)를 1 더함
            
        else:
            count_dict[n] = 1 # 없으면 새로 추가하면서 1로 시작
    
    max_count = max(count_dict.values())
    
    most_freq = [] # 가장 많이 나온 숫자가 몇 개인지 확인
    for key in count_dict:
        if count_dict[key] == max_count:
            most_freq.append(key)
    
    if len(most_freq) > 1: # 최빈값이 여러 개면 -1, 하나면 그 값을 리턴
        return -1
    else:
        return most_freq[0]
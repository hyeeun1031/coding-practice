import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()
    
    # 2단계: 허용된 문자만 남기기
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 마침표 2개 이상 → 하나로
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 'a'
    if not new_id:
        new_id = 'a'
    
    # 6단계: 길이 15자 제한 + 끝 마침표 제거
    new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이 3 미만이면 마지막 문자 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id

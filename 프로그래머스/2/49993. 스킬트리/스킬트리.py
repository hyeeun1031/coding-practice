def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        # skill에 해당하는 문자만 순서대로 추출
        filtered = [c for c in tree if c in skill]
        # 추출된 순서가 skill의 앞부분과 같은지 확인
        if filtered == list(skill[:len(filtered)]):
            answer += 1
    return answer
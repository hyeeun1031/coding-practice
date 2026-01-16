def solution(nums):
    unique_cnt = len(set(nums))   # 서로 다른 폰켓몬 종류 수
    pick_cnt = len(nums) // 2     # 선택해야 하는 폰켓몬 수
    return min(unique_cnt, pick_cnt)

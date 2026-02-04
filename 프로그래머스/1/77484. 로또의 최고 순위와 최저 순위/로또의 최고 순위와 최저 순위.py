def solution(lottos, win_nums):
    # 1) 0(알아볼 수 없는 번호) 개수
    zero_cnt = lottos.count(0)
    
    # 2) 0이 아닌 번호 중 당첨 번호와 겹치는 개수
    match_cnt = 0
    for num in lottos:
        if num != 0 and num in win_nums:
            match_cnt += 1

    # 3) 최고 / 최저로 맞출 수 있는 개수
    max_match = match_cnt + zero_cnt  # 0이 전부 당첨 번호라고 가정
    min_match = match_cnt             # 0이 전부 꽝이라고 가정

    # 4) 맞춘 개수를 등수로 변환하는 함수
    def get_rank(count):
        if count <= 1:  # 0개 또는 1개 맞추면 6등
            return 6
        return 7 - count  # 그 외는 7 - 맞춘개수

    max_rank = get_rank(max_match)
    min_rank = get_rank(min_match)

    return [max_rank, min_rank]

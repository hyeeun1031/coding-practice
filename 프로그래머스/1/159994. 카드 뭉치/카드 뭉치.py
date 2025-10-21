def solution(cards1, cards2, goal):
    i, j = 0, 0  # 각 카드 뭉치의 포인터

    for word in goal:
        # cards1에서 사용할 수 있는 경우
        if i < len(cards1) and cards1[i] == word:
            i += 1
        # cards2에서 사용할 수 있는 경우
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        # 둘 다 아닌 경우 -> 불가능
        else:
            return "No"
    
    return "Yes"

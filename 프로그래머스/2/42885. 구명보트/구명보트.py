def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람도 함께 탑승
        right -= 1     # 무거운 사람은 반드시 탑승
        boats += 1

    return boats

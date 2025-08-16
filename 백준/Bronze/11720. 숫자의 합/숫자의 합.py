n = int(input()) # 숫자의 개수
numbers = input().strip() # 숫자들을 문자열로 입력받음

print(sum(map(int, numbers))) # 각 자리 숫자를 더해서 출력
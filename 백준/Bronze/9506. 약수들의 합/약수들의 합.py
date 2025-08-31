import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:  # 입력 종료
        break

    divisors = []
    total = 0
    limit = int(n**0.5)

    # 약수 구하기 (1부터 √n까지)
    for i in range(1, limit + 1):
        if n % i == 0:
            j = n // i
            if i != n:
                divisors.append(i)
                total += i
            if j != i and j != n:
                divisors.append(j)
                total += j

    divisors.sort()  # 오름차순 정렬

    if total == n:
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")

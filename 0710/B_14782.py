def divisiors(num):
    ans = 0
    for i in range(1, num + 1):
        if num % i == 0: ans += i
    print(ans)
divisiors(int(input()))
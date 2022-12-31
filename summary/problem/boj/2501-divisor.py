N, K = map(int, input().split())


def solution():
    cnt = 0

    for i in range(N):
        if (N % (i + 1) == 0):
            cnt += 1
            if (cnt == K):
                print(i + 1)
                return

    print(0)


solution()

import sys
input = sys.stdin.readline

T = int(input())
cnt = 0
for tc in range(T):
    s, e = map(int, input().split())

    d = e-s

    rd = d**(1/2)
    # print(rd)

    if int(rd)**2 + int(rd) < d:
        cnt = 2*int(rd) + 1

    elif int(rd)**2 == d:
        cnt = 2*(int(rd)) - 1

    elif d <= int(rd)**2 + int(rd):
        cnt = 2*int(rd)

    print(cnt)

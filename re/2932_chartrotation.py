import sys
from copy import deepcopy
input = sys.stdin.readline

N, K = map(int, input().split())

mat = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        cnt += 1
        mat[i][j] = cnt
print(mat)


for _ in range(K):
    cnt = 0
    x, r, c = map(int, input().split())

    # if x % N == 0:      #나머지가 0이면
    #     nr = x//N -1    #현재 좌표 r
    # else:
    #     nr = x//N
    #
    # nc = N - (x%N) -1   #현재 좌표 c
    nr, nc = 0, 0
    flag = True
    for i in range(N):
        for j in range(N):
            if mat[i][j] == x:
                nr, nc = i, j
                break
        if not flag:
            break

    arr = deepcopy(mat[nr])
    diff = c - nc

    print(diff)
    for j in range(N):
        nj = j+diff
        if nj < 0:
            nj = N + nj

        # print(nj)
        mat[nr][nj] = arr[j]

        if nj >=N:
            nj = N%nj

        mat[nr][nj] = arr[j]



    print(mat)









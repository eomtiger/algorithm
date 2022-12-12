import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def move(direction, value_sum, stage, j):

    global minV
    # if value_sum < check[stage][j]:
    #     check[stage][j] = value_sum
    # else:
    #     return
    check[stage][j] = value_sum

    if value_sum >= minV:
        return

    if stage == N-1:
        if value_sum < minV:
            minV = value_sum
        return

    dir = [0, 1, 2]
    if stage != 0:
        dir.remove(direction)

    for i in dir:
        if i == 0 and 0 <= j-1 < M and check[stage+1][j-1] > value_sum + mat[stage+1][j-1]:    #왼쪽 아래
            move(i, value_sum + mat[stage+1][j-1], stage+1, j-1)

        if i == 1 and check[stage+1][j] > value_sum + mat[stage+1][j]:                      #바로 아래
            move(i, value_sum + mat[stage+1][j], stage+1, j)

        if i == 2 and 0 <= j+1 < M and check[stage+1][j+1] > value_sum + mat[stage+1][j+1]:    #오른쪽 아래
            move(i, value_sum + mat[stage+1][j+1], stage+1, j+1)


N, M = map(int, input().split())

minV = 987654321
mat = [list(map(int, input().split())) for _ in range(N)]

check = [[987654321] * M for _ in range(N)]
# print(check)
for j in range(len(mat[0])):
    move(0, mat[0][j], 0, j)  #내려온 방향, 지금까지 비용, 층, j 좌표

# print(check)
print(minV)
import copy

N, B = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

m1 = copy.deepcopy(mat)


for _ in range(B-1):
    m2 = copy.deepcopy(mat)
    for i in range(N):
        for j in range(N):
            val = 0
            for k in range(N):
                val += mat[i][k] * m1[k][j]
                # print((i,j), val)
            m2[i][j] = val
    mat = m2


for i in range(N):
    for j in range(N):
        mat[i][j] = mat[i][j] % 1000

# print(mat)

for i in range(N):
    l = ''
    for j in range(N):
        if j == N-1:
            l += str(mat[i][j])
        else:
            l += (str(mat[i][j])+ ' ')
    print(l)


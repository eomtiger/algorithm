def move(loc,):
    if mat[loc[0]][loc[1]] == 0:
        mat[loc[0]][loc[1]] = 2
    
    for i in range(4):
        



N, M = map(int, input().split())

r, c, d = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

loc = (r, c)
print(mat)
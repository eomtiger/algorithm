import sys
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

def move(visited, loc, cnt):

    global res

    cnt += 1
    # print(visited, cnt)
    for i in range(4):
        # print('cnt:', cnt, 'i:', i, visited)
        if 0 <= loc[0]+dy[i] < R and 0 <= loc[1]+dx[i] < C:
            if mat[loc[0]+dy[i]][loc[1]+dx[i]] not in visited:
                # print(cnt, i)
                visited.add(mat[loc[0] + dy[i]][loc[1] + dx[i]])
                move(visited, [loc[0]+dy[i], loc[1]+dx[i]], cnt)
                visited.remove(mat[loc[0] + dy[i]][loc[1] + dx[i]])

    if cnt > res:
        res = cnt

R, C = map(int, input().split())

mat = [list(input().rstrip()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]



res = 0
cnt = 0
visited = set(mat[0][0])
loc = [0, 0]

move(visited, loc, cnt)

print(res)

# r, c = map(int, input().split())
# maps = []
# for _ in range(r):
#     maps.append(list(input()))
# ans = 0
# alphas = set()
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y, count):
#     global ans
#     ans = max(ans, count)
#     for i in range(4):
#         # print('cnt:', count, 'i:', i, alphas)
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
#             alphas.add(maps[nx][ny])
#             dfs(nx, ny, count+1)
#             alphas.remove(maps[nx][ny])
# alphas.add(maps[0][0])
# dfs(0, 0, 1)
# print(ans)

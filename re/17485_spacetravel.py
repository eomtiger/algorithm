import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
board = [[INF] + list(map(int, input().split())) + [INF] for _ in range(N)]

print(board)

DP = [[(0, 0, 0) for i in range(M+2)] for j in range(N)]
print(DP)
for first_dp in range(1, M+1):
    DP[1][first_dp] = (board[1][first_dp] + board[0][first_dp - 1],
                       board[1][first_dp] + board[0][first_dp],
                       board[1][first_dp] + board[0][first_dp + 1])

print(DP)
for x in range(2, N):
    DP[x][1] = (INF,
                board[x][1] + min(DP[x - 1][1][0], DP[x - 1][1][2]),
                board[x][1] + min(DP[x - 1][2][0], DP[x - 1][2][1]))
    DP[x][M] = (board[x][M] + min(DP[x - 1][M - 1][1], DP[x - 1][M - 1][2]),
                board[x][M] + min(DP[x - 1][M][0], DP[x - 1][M][2]),
                INF)
    for y in range(2, M):
        DP[x][y] = (board[x][y] + min(DP[x - 1][y - 1][1], DP[x - 1][y - 1][2]),
                    board[x][y] + min(DP[x - 1][y][0], DP[x - 1][y][2]),
                    board[x][y] + min(DP[x - 1][y + 1][0], DP[x - 1][y + 1][1]))
print(min(map(min, DP[N-1][1:M+1])))
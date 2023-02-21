N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]



dp = [[0, 0, 0] for i in range(N)]



for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = mat[i][j]

        else:
            if j == 0:
                dp[i][j] = min(mat[i][j] + dp[i-1][j+1], mat[i][j] + dp[i-1][j+2])

            elif j == 1:
                dp[i][j] = min(mat[i][j] + dp[i-1][j-1], mat[i][j] + dp[i-1][j+1])

            else:
                dp[i][j] = min(mat[i][j] + dp[i-1][j-2], mat[i][j] + dp[i-1][j-1])

print(min(dp[-1]))
                



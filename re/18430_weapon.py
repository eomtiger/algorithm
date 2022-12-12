N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

visited = set()
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            maxV = 0
            #좌상


    #우상#좌하#우하
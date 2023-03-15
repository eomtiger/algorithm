T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    matB = [list(map(int, input().split())) for _ in range(N)]
    # print(matB)
    #      상태, 시간, 생명력
    mat = [[[-1, -1, -1] for _ in range(K+M)] for _ in range(K+N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(K//2, K//2+N):
        for j in range(K//2, K//2+M):
            if matB[i-K//2][j-K//2]:
                mat[i][j] = [0, 0, matB[i-K//2][j-K//2]]

    # print(mat)

    t = 0
    while t != K:
        visited = set()
        # print(t, mat[152][151])
        for i in range(K+N):
            for j in range(K+M):
                if (i,j) not in visited and mat[i][j][0] == 0: #상태가 비활성이라면
                    mat[i][j][1] += 1 # 한시간 추가하고
                    if mat[i][j][1] == mat[i][j][2]: #시간 == 생명력이라면
                        mat[i][j][0] = 1 # 상태는 활성

                elif mat[i][j][0] == 1: #상태가 활성이라면
                    mat[i][j][1] += 1 # 한시간 추가
                    if mat[i][j][1] == mat[i][j][2]*2: #시간 == 생명력*2라면
                        mat[i][j][0] = 2 # 상태는 죽음
                    if mat[i][j][1] == mat[i][j][2]+1: # 시간 == 생명력 +1이라면
                        for d in range(4): #사방 탐색을 진행
                            if mat[i+dy[d]][j+dx[d]][0] == -1: # 옮겨간 곳이 비었다면
                                # if i == K//2 and j ==K//2:
                                    # print((i+dy[d], j+dx[d]))
                                mat[i+dy[d]][j+dx[d]] = [0, 0, mat[i][j][2]]
                                visited.add((i+dy[d], j+dx[d]))
                                
                            elif (i+dy[d], j+dx[d]) in visited and mat[i+dy[d]][j+dx[d]][0] == 0 and mat[i+dy[d]][j+dx[d]][1] == 0: #옮겨간 곳이 차있고
                                if mat[i+dy[d]][j+dx[d]][2] < mat[i][j][2]:     #생명력이 낮다면
                                    mat[i+dy[d]][j+dx[d]][2] = mat[i][j][2]     #생명력을 갈아낌
        t += 1 
        

    ans = 0
    for i in range(K+N):
        for j in range(K+M):
            if mat[i][j][0] == 0 or mat[i][j][0] == 1:
                ans += 1
                # print(i,j)

    print(f'#{tc} {ans}')






            
            
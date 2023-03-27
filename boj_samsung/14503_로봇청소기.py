def move(r, c, d, mat):
    global cnt 
    if mat[r][c] == 0:          #1번 아직 청소가 안됐으면 청소
        mat[r][c] = 2
        cnt += 1

    flag = False                #다음에 갈 곳이 없다고 가정 처음엔
    for i in range(4):
        if 0 <= r+dy[i] < N and 0 <= c+dx[i] < M:     #다음이 벽이 아니고
            if not mat[r+dy[i]][c+dx[i]]:             # 다음이 0이면
                flag = True                           #갈 곳이 있다는 것이다

    if not flag: # 갈 곳이 없다면
        if 0 <= r+dy[(d+2)%4] < N and 0 <= c+dx[(d+2)%4] < M: # 진행방향의 반대방향 다음 한칸이 범위에 있고
            if mat[r+dy[(d+2)%4]][c+dx[(d+2)%4]] != 1:           #그곳이 벽이 아니라면
                move(r+dy[(d+2)%4], c+dx[(d+2)%4], d, mat )   #후진하자
        else:
            return

    elif flag:  # 갈 곳이 있다면
        stop = False
        while not stop:
            d = (d+3)%4 #반시계로 90도 회전
            if 0 <= r+dy[d] < N and 0 <= c+dx[d] < M: #다음이 영역 안에 잇고
                if mat[r+dy[d]][c+dx[d]] == 0:  # 청소안된곳이라면
                    stop =True
                    move(r+dy[d], c+dx[d], d, mat )   # 다음으로 가자
                
                if stop:
                    break



N, M = map(int, input().split())

r, c, d = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,0,1,0] #북동남서
dx = [0,1,0,-1] #0123

cnt = 0

move(r, c, d, mat)

print(cnt)
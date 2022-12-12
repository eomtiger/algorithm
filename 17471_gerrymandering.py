def dfs(sel, sel2):             #두개 선거구를 너비우선탐색 , 깊이도 상관없을듯
    global N, M
    flag = False                #flag 설정
    q = []
    visited = []
    q.append(sel[0])
    visited.append(sel[0])

    while len(q) != 0:
        for i in range(1, N+1):             #이동한 곳이 선거구 안에 있다면
            if mat[q[0]][i] == 1 and i not in visited and i in sel:
                q.append(i)
                visited.append(i)
        # print(q)
        q.pop(0)
        # print(q)
    # print(visited)
    if set(sel) - set(visited) == set():    #선거구와 방문한 곳을 차집합
        flag = True

    ######################################### 위와 같이 선거구 두번째
    q = []
    visited = []
    q.append(sel2[0])
    visited.append(sel2[0])

    while len(q) != 0:
        for i in range(1, N + 1):
            if mat[q[0]][i] == 1 and i not in visited and i in sel2:
                q.append(i)
                visited.append(i)
        q.pop(0)

    if set(sel2) - set(visited) != set():
        flag = False

    return flag



def combination(idx, sidx):
    global N, M, minV

    if sidx == M:
        sel2 = [x for x in arr if x not in sel] #첫번째 선거구가 정해지면 나머지 선거구도 만듬


        # print(dfs(sel, sel2))
        if dfs(sel, sel2):
            p1 = 0                              #첫 선거구의 인구 수
            for i in range(len(sel)):
                p1 += info[str(sel[i])][1]
            p2 = 0                              #두번째 선거구의 인구 수
            for j in range(len(sel2)):
                p2 += info[str(sel2[j])][1]

            if abs(p1-p2) < minV:           #인구수 차
                minV = abs(p1-p2)


        return

    if idx == N:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


N = int(input())

p = list(map(int, input().split()))  #인구 수
mat = [[0]*(N+1) for _ in range(N+1)]   #인접행렬
info = {}                           #하나의 지역 당 정보
arr = []                            #전체 지역 배열
for i in range(1, N+1):
    edges = list(map(int, input().split())) #첫 원소는 edge개수
    edges.pop(0)
    info[str(i)] = [set(edges), p[i-1]]

    arr.append(i)
# print(mat)
# print(info)
# print(info[str(1)][0])
minV = 987654321
for i in range(1, N+1):
    for j in range(1, N+1):
        if j in info[str(i)][0]:
            mat[i][j] = 1           #인접행렬 완성
            # mat[j][i] = 1
# print(mat)
# print(arr)

for i in range(1, N//2 +1):         #조합을 이용해서 지역 수를 2로 나눈 몫만큼 돌림
                                    #조합 특성 상 앞과 뒤가 같음
    sel = [0]*i
    M = len(sel)
    combination(0, 0)
if minV == 987654321:
    minV = -1
print(minV)

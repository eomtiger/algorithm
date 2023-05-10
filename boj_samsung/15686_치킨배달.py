def combination(ch_comb, stage, loc): # [], 1, 0
    global ch_list, M, homes, res
    if stage == M+1:
        # print(ch_comb)
        for home in homes:  # 집 좌표를 뽑는다
            for ch in ch_comb:  # 치킨 집 좌표를 뽑는다
                d = abs(home[0] - ch[0]) + abs(home[1] - ch[1])
                homes[home] = min(d, homes[home])
        # print(homes)
        total = 0
        for home in homes:
            total += homes[home]
            homes[home] = 987654321
        if total < res:
            res = total
        # print(ch_comb)
        return
    for i in range(loc, len(ch_list)-M+stage):    # [1,2,3,4,5]
        ch_comb.append(ch_list[i])
        combination(ch_comb, stage+1, i+1)
        ch_comb.pop()

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

ch_list = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 2:
            ch_list.append((i,j))

homes = {}
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            homes[(i, j)] = 987654321
res = 987654321
flag = True
if len(ch_list) <= M: #치킨 집 개수가 한계점(M)보다 작거나 같다면
    for home in homes:  #집 좌표를 뽑는다
        for ch in ch_list: #치킨 집 좌표를 뽑는다
            d = abs(home[0] - ch[0]) + abs(home[1] - ch[1])
            homes[home] = min(d, homes[home])


 # 치킨 집 개수가 한계점보다 많다면

else:
    flag = False
    combination([], 1, 0)

if flag:
    res = 0
    for home in homes:
        res += homes[home]

print(res)

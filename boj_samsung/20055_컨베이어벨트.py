from collections import deque

N, K = map(int, input().split())

arr = deque(list(map(int, input().split())))

# print(N, K, arr)

arrR = deque([0] * N)

# print(arrR)
flag = 0
round = 0
while flag < K:
    
    round += 1
    #먼저 로봇과 벨트가 한칸씩 이동한다
    # for i in range(N-1):
    #     if arrR[i] == 1:
    #         arr[i] -= 1
    #         if arr[i] == 0:
    #             flag += 1
    # if flag == K:
    #     break
    arr.appendleft(arr.pop())
    arrR.appendleft(arrR.pop())
    # arrR[0] = 0 #첫 칸은 0이됨
    arrR[-1] = 0 #마지막 칸도 0이 됨
    # print(arr)
    # print(arrR)
    # print('11111111111111111111')
    

    #가장 먼저 올라간 로봇부터 한칸 씩 이동
    for i in range(N-2, -1, -1):
        
        if arrR[i]==1 and arr[i+1] > 0 and arrR[i+1] == 0: #한 칸 옆이 내구도가 0보다 크고 로봇이 없다면
            arr[i+1] -=1  # 벨트 내구도 하나 깎고
            arrR[i] = 0 # 그 자리를 떠나
            arrR[i+1] = 1 # 옆으로 로봇 옮김
            if i+1 == N-1: # 옆자리가 제일 끝이라면
                arrR[N-1] = 0 #빈자리가 된다

            if arr[i+1] <= 0: #옆자리 내구도가 0이면
                flag += 1       #flag에 1을 더하고
            if flag == K:       # flag == K 이면 끝내
                break
    if flag == K: 
        break
    # print(arr)
    # print(arrR)
    # print('222222222222222')
    #올리는 위치의 내구도가 0이 아니면
    if arr[0] != 0:
        arrR[0] = 1 #첫 칸에 로봇을 올리고
        arr[0] -= 1 # 첫 칸 내구도 깎음
        if arr[0] == 0: #첫칸 내구도가 0이 되고
            flag+=1     # flag에 1을 더함
    # print(arr)
    # print(arrR)
    # print('3333333333333333')
    if flag == K:   # flag==K면
        break       # 끝내

print(round)



    
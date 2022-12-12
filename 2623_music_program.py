import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [[0]*(N+1) for _ in range((N+1))]  #인접행렬을 만들자

order_list = []                          #순서들을 리스트로 담자
for i in range(M):
    a = list(map(int, input().split()))
    a.pop(0)                            #개수는 제외하고
    order_list.append(a)                #리스트에 담자
#ex) [[1,4,3], [6,2,5,4], [2,3]] => order_list

for order in order_list:                    #인접행렬을 만들자
    for i in range(0, len(order)-1):        #order에서 마지막 원소 전까지 for문
        for j in range(i+1, len(order)):    #위에서 정한 원소 다음 원소부터 마지막 원소까지
            mat[order[i]][order[j]] = 1     #i보다 j가 순서상 뒤에 있다는 것을 인접행렬에 표시

# print(mat)

arr = []        #배열을 만들자
for i in range(1,N+1):
    arr.append(i)

# print(arr)
#dfs 깊이우선 탐색
stack = [1]
visited = [1]
res = []
flag = True
while stack and flag:
    # print(stack)
    # print('r',res)
    cnt = 0
    for i in range(len(arr)):
        if mat[stack[-1]][arr[i]] == 1 and arr[i] in stack:         #스택에 같은 가수가 두 번 들어온다면 순서가 엉킨 것
            flag = False                                            #순서 정렬이 불가
            break
        elif mat[stack[-1]][arr[i]] == 1 and arr[i] not in visited:
            stack.append(arr[i])
            visited.append(arr[i])
            cnt+=1                                                  #자신 다음 순서가 추가될 때 하나 늘림

    if cnt == 0:            #더 이상 자신 뒤로 순서가 없다면
        a = stack.pop()     #스택에서 꺼내서
        res.insert(0, a)    #결과 리스트 맨 앞으로 삽입
    # print(stack)

    if len(stack) == 0:             #스택이 모두 비었을 때
        for i in arr:               #아직 visited에 없는 가수를 stack에 추가해주고
            if i not in visited:    #while문을 다시 돌리기
                stack.append(i)
                visited.append(i)
                break
if not flag:
    print(0)
else:
    for i in res:
        print(i)







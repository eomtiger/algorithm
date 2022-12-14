import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

mat = [[0]*N for _ in range(N)]     #dp 배열을 만들어주고

for d in range(N):                  #시작과 끝의 차이를 d라고 하고
    for st in range(N-d):           #d가 0 일 때, 시작은 0부터 N-1까지
                                    #d가 1 일 때, 시작은 0부터 N-2까지
                                    #....
                                    #d가 N-1일 때, 시작은 0뿐

        end = st+d                  #끝은 시작 +d

        if st == end:               #시작과 끝이 같다면 길이가 1이므로 그냥 palindrome
            mat[st][end] = 1        #dp배열에 추가


        elif arr[st] == arr[end] and d ==1: #시작과 끝이 같은데 길이가 2, 시작과 끝의 차이가 1이면
            mat[st][end] = 1                #palinedrome으로 배열에 추가

        elif arr[st] == arr[end] and mat[st+1][end-1] == 1:
        #시작과 끝이 같고, 배열에서 시작+1과 끝-1이 palindrome을 확인한다면
        #이 역시 palindrome
            mat[st][end] = 1


for _ in range(M):
    s, e = map(int, input().split())

    print(mat[s-1][e-1])


    ###### dp로 풀기 전 그냥 탐색 == 시간초과과###########
    # flag = True
    # for i in range(((e-s)//2)//2 +1):
    #    # print('s:', s, 'e:', e, arr[s-1+i], arr[e-1-i])
    #     if arr[s-1+i] != arr[e-1-i]:        #양끝이 다르면
    #         flag = False
    #         break
    #
    #     elif arr[s-1+(e-s)//2-i] != arr[e-1-(e-s)//2+i]:    #가운데가 다르면
    #         flag = False
    #         break

    # else:
    #     for i in range((e-s)//2+1):
    #
    #         if arr[s-1+i] == arr[e-1-i]:
    #             pass
    #         else:
    #             flag = False
    #             break

    # if flag:
    #     print(1)
    # else:
    #     print(0)
# T = int(input())

# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     matB = [list(map(int, input().split())) for _ in range(N)]
#     print(matB)

    # m = {}
    # for i in range(N):
    #     for j in range(M):
    #         m[(i,j)] = [mat[i][j], 0, 0]

    # t = 0
    # a = {}
    # dy = [-1, 1, 0, 0]
    # dx = [0, 0, -1, 1]
    # while t != 1:
    #     for key in m.keys():
    #         if m[key][0] and m[key][0] <= m[key][1] < m[key][0]*2:
    #             for i in range(4):
    #                 print()

    #         elif m[key][0] and m[key][0]*2 <= m[key][1]:              

                    
    #     t+= 1

from collections import deque

a = [1,2,3,4,5,6]

a = deque(a)

print(a)
a.append(6)
print(a)
a.pop()
print(a)
a.appendleft(0)
print(a)


            
            
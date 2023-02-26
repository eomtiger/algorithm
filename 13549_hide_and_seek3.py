# import time # time 라이브러리 import
# start = time.time() # 시작
#
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

T = 987654321

record = {}

def move(N, t):
    # print(N, t)
    # print(record)
    global T
    if t > T:            #움직인 시간이 글로벌 time보다 크다면
        return              #리턴

    if record.get(N) and record[N] <= t:
        #record에 N을 키로 갖는 값이 있고 value가 t보다 작다면
        return
    else:
        record[N] = t

    # if N in record:
    #     return
    # else:
    #     record.add(N)


    if N >= K:              # N이 K보다 크거나 같다면
        t += N-K            # -1로 걷기만 가능
        T = min(T, t) # N-K만큼 시간을 더하고 글로벌 time과 비교
        return

    move(2*N, t)
    move(N+1, t+1)
    move(N-1, t+1)

move(N, 0)

print(T)
#
#
# # print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력



###############################################################################

from collections import deque

N, K = map(int, input().split())

visited = set()
visited.add(N)
t_arr = [0]*100001
res = 0
q = deque()
q.append(N)


while q:

    a = q.popleft()

    if a == K:

        res = t_arr[a]
        break

    if 0 <= 2*a <= 100000 and 2*a not in visited:
        q.appendleft(2*a)
        t_arr[2*a] = t_arr[a]
        visited.add(2*a)

    for k in (a+1, a-1):
        if 0 <= k <= 100000 and k not in visited:
            q.append(k)
            t_arr[k] = t_arr[a] + 1
            visited.add(k)

print(res)


from collections import deque

mat = [list(input()) for _ in range(4)]

for i in range(4):
    for j in range(8):
        mat[i][j] = int(mat[i][j])

t1 = deque(mat[0])
t2 = deque(mat[1])
t3 = deque(mat[2])
t4 = deque(mat[3])


K = int(input())

li = [list(map(int, input().split())) for _ in range(K)]
# print(mat)
# print(li)


# print(t_li)
t_li = []
for i in range(len(li)):

    t_li.append((t1[2], t2[6]))
    t_li.append((t2[2], t3[6]))
    t_li.append((t3[2], t4[6]))


    if li[i][0] == 1: # 1번 톱니가 돌 때
        if t_li[0][0] == t_li[0][1]: #1,2번 톱니가 같은 극이면
            if li[i][1] == -1:  # 반시계 방향이면
                a = t1.popleft()
                t1.append(a)

            elif li[i][1] == 1:  # 시계방향이면
                a = t1.pop()
                t1.appendleft(a)
        elif t_li[0][0] != t_li[0][1]: # 1,2번 톱니가 다른 극이면
            if t_li[1][0] == t_li[1][1]: # 2,3번 톱니가 같은 극이면
                if li[i][1] == -1: #반시계 방향이면
                    a = t1.popleft() #1번은 반시계 2번은 시계방향이동
                    t1.append(a)
                    b = t2.pop()
                    t2.appendleft(b)
                elif li[i][1] == 1: # 시계방향이면
                    a = t1.pop()
                    t1.appendleft(a)
                    b = t2.popleft()
                    t2.append(b)
            elif t_li[1][0] != t_li[1][1]: #2, 3번 톱니가 다른 극이면
                if t_li[2][0] == t_li[2][1]: # 3,4번 톱니가 같은 극이면
                    if li[i][1] == -1:  # 반시계 방향이면
                        a = t1.popleft()  # 1번은 반시계 2번은 시계방향이동
                        t1.append(a)
                        b = t2.pop()
                        t2.appendleft(b)
                        c = t3.popleft()
                        t3.append(c)
                    elif li[i][1] == 1:  # 시계방향이면
                        a = t1.pop()
                        t1.appendleft(a)
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)
                elif t_li[2][0] != t_li[2][1]: # 3,4번 톱니가 다른 극이면
                    if li[i][1] == -1:  # 반시계 방향이면
                        a = t1.popleft()  # 1번은 반시계 2번은 시계방향이동
                        t1.append(a)
                        b = t2.pop()
                        t2.appendleft(b)
                        c = t3.popleft()
                        t3.append(c)
                        d = t4.pop()
                        t4.appendleft(d)

                    elif li[i][1] == 1:  # 시계방향이면
                        a = t1.pop()
                        t1.appendleft(a)
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)
                        d = t4.popleft()
                        t4.append(d)

        print('1', t1,t2,t3,t4)
    elif li[i][0] == 2: #2번 톱니가 돌때

        if t_li[0][0] == t_li[0][1]:  # 1,2번 톱니가 같은 극이면
            if t_li[1][0] == t_li[1][1]: #2,3번 톱니가 같으면
                if li[i][1] == -1:  # 2번이 반시계로 돌때
                    b = t2.popleft()
                    t2.append(b)

                elif li[i][1] == 1:  # 시계방향
                    b = t2.pop()
                    t2.append(b)

            elif t_li[1][0] != t_li[1][1]: #2,3번 톱니가 다르면
                if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같으면
                    if li[i][1] == -1: #2번이 반시계로 돌때
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)

                    elif li[i][1] == 1: #시계방향
                        b = t2.pop()
                        t2.append(b)
                        c = t3.popleft()
                        t3.append(c)

                elif t_li[2][0] != t_li[2][1]: #3,4 번 톱니가 다르면
                    if li[i][1] ==  -1: #반시계
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)
                        d = t4.popleft()
                        t4.append(d)

                    elif li[i][1] == 1: #시계
                        b = t2.pop()
                        t2.appendleft(b)
                        c = t3.popleft()
                        t3.append(c)
                        d = t4.pop()
                        t4.appendleft(d)


        elif t_li[0][0] != t_li[0][1]:  # 1,2번 톱니가 다른 극이면

            if t_li[1][0] == t_li[1][1]: #2,3번 톱니가 같으면

                if li[i][1] == -1:  # 2번이 반시계로 돌때
                    b = t2.popleft() ##################################################################3
                    t2.append(b)
                    a = t1.pop()
                    t1.appendleft(a)

                elif li[i][1] == 1: #시계 방향
                    b = t2.pop()
                    t2.appendleft(b)
                    a = t1.popleft()
                    t1.append(a)

            elif t_li[1][0] != t_li[1][1]: #2,3번 톱니가 다르면

                if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같으면

                    if li[i][1] == -1: #2번이 반시계로 돌때
                        a = t1.pop()
                        t1.appendleft(a)
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)

                    elif li[i][1] == 1: #시계방향
                        a = t1.popleft()
                        t1.append(a)
                        b = t2.pop()
                        t2.append(b)
                        c = t3.popleft()
                        t3.append(c)

                elif t_li[2][0] != t_li[2][1]: #3,4 번 톱니가 다르면

                    if li[i][1] ==  -1: #반시계
                        a = t1.pop()
                        t1.appendleft(a)
                        b = t2.popleft()
                        t2.append(b)
                        c = t3.pop()
                        t3.appendleft(c)
                        d = t4.popleft()
                        t4.append(d)

                    elif li[i][1] == 1: #시계
                        a = t1.popleft()
                        t1.append(a)
                        b = t2.pop()
                        t2.appendleft(b)
                        c = t3.popleft()
                        t3.append(c)
                        d = t4.pop()
                        t4.appendleft(d)


        print('2',t1,t2,t3,t4)

    elif li[i][0] == 3: #3번 톱니가 돌 때
        if t_li[2][0] == t_li[2][1]:  # 3,4번 톱니가 같은 극이면
            if t_li[1][0] == t_li[1][1]:  # 2,3번 톱니가 같으면
                if li[i][1] == -1:  # 3번이 반시계로 돌때
                    c = t3.popleft()
                    t3.append(c)

                elif li[i][1] == 1:  # 시계방향
                    c = t3.pop()
                    t3.append(c)

            elif t_li[1][0] != t_li[1][1]:  # 2,3번 톱니가 다르면
                if t_li[0][0] == t_li[0][1]:  # 1,2번 톱니가 같으면
                    if li[i][1] == -1:  # 3번이 반시계로 돌때
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                    elif li[i][1] == 1:  # 시계방향
                        c = t3.pop()
                        t3.append(c)
                        b = t2.popleft()
                        t2.append(b)
                elif t_li[2][0] != t_li[2][1]:  # 1,2 번 톱니가 다르면
                    if li[i][1] == -1:  # 반시계
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                        a = t1.popleft()
                        t1.append(a)
                    elif li[i][1] == 1:  # 시계
                        c = t3.pop()
                        t3.appendleft(c)
                        b = t2.popleft()
                        t2.append(b)
                        a = t1.pop()
                        t1.appendleft(a)

        elif t_li[2][0] != t_li[2][1]:  # 3,4번 톱니가 다른 극이면
            if t_li[1][0] == t_li[1][1]:  # 2,3번 톱니가 같으면
                if li[i][1] == -1:  # 3번이 반시계로 돌때
                    d = t4.pop()
                    t4.appendleft(d)
                    c = t3.popleft()
                    t3.append(c)
                elif li[i][1] == 1:  # 시계 방향
                    d = t4.popleft()
                    t4.append(d)
                    c = t3.pop()
                    t3.appendleft(c)
            elif t_li[1][0] != t_li[1][1]:  # 2,3번 톱니가 다르면
                if t_li[2][0] == t_li[2][1]:  # 1,2번 톱니가 같으면
                    if li[i][1] == -1:  # 3번이 반시계로 돌때
                        d = t4.pop()
                        t4.appendleft(d)
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                    elif li[i][1] == 1:  # 시계방향
                        d = t4.popleft()
                        t4.append(d)
                        c = t3.pop()
                        t3.append(c)
                        b = t2.popleft()
                        t2.append(b)
                elif t_li[2][0] != t_li[2][1]:  # 1,2 번 톱니가 다르면
                    if li[i][1] == -1:  # 반시계
                        d = t4.pop()
                        t4.appendleft(d)
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                        a = t1.popleft()
                        t1.append(a)
                    elif li[i][1] == 1:  # 시계
                        d = t4.popleft()
                        t4.append(d)
                        c = t3.pop()
                        t3.appendleft(c)
                        b = t2.popleft()
                        t2.append(b)
                        a = t1.pop()
                        t1.appendleft(a)
        print('3',t1,t2,t3,t4)

    elif li[i][0] == 4: # 4번 톱니가 돌 때
        if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같은 극이면
            if li[i][1] == -1:  # 반시계 방향이면
                d = t4.popleft()  # 4번은 반시계 3번은 시계방향이동
                t4.append(d)

            elif li[i][1] == 1:  # 시계방향이면
                d = t4.pop()
                t4.appendleft(d)

        elif t_li[2][0] != t_li[2][1]: # 3,4번 톱니가 다른 극이면
            if t_li[1][0] == t_li[1][1]: # 2,3번 톱니가 같은 극이면
                if li[i][1] == -1: #반시계 방향이면
                    d = t4.popleft() #4번은 반시계 3번은 시계방향이동
                    t4.append(d)
                    c = t3.pop()
                    t3.appendleft(c)
                elif li[i][1] == 1: # 시계방향이면
                    d = t4.pop()
                    t4.appendleft(d)
                    c = t3.popleft()
                    t3.append(c)
            elif t_li[1][0] != t_li[1][1]: #2, 3번 톱니가 다른 극이면
                if t_li[0][0] == t_li[0][1]: # 1,2번 톱니가 같은 극이면
                    if li[i][1] == -1:  # 반시계 방향이면
                        d = t4.popleft()  # 1번은 반시계 2번은 시계방향이동
                        t4.append(d)
                        c = t3.pop()
                        t3.appendleft(c)
                        b = t2.popleft()
                        t2.append(b)
                    elif li[i][1] == 1:  # 시계방향이면
                        d = t4.pop()
                        t4.appendleft(d)
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                elif t_li[0][0] != t_li[0][1]: # 1,2번 톱니가 다른 극이면
                    if li[i][1] == -1:  # 반시계 방향이면
                        d = t4.popleft()  # 1번은 반시계 2번은 시계방향이동
                        t4.append(d)
                        c = t3.pop()
                        t3.appendleft(c)
                        b = t2.popleft()
                        t2.append(b)
                        a = t1.pop()
                        t1.appendleft(a)
                    elif li[i][1] == 1:  # 시계방향이면
                        d = t4.pop()
                        t4.appendleft(d)
                        c = t3.popleft()
                        t3.append(c)
                        b = t2.pop()
                        t2.appendleft(b)
                        a= t1.popleft()
                        t1.append(a)
        print('4',t1,t2,t3,t4)
    t_li.clear()

# print(t1)
# print(t2)

total = 0
if t1[0] == 0:
    pass
elif t1[1] == 1:
    total+=1

if t2[0] == 0:
    pass
else:
    total+=2
if t3[0] == 0:
    pass
else:
    total+=4

if t4[0] == 0:
    pass
else: total+=8

print(total)
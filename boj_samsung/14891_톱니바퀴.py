from collections import deque

mat = [deque(list(input())) for _ in range(4)]

for i in range(4):
    for j in range(8):
        mat[i][j] = int(mat[i][j])

# print(mat)


K = int(input())

li = [list(map(int, input().split())) for _ in range(K)]


# print(li)

def moveleft(start, direction):
    global mat
    d = direction
    rotate_list = []
    for i in range(start-2, -1, -1):
        if mat[i+1][6] == mat[i][2]: #오른쪽 바퀴와 i번째 바퀴의 맞닿은 극이 같으면
            break
        else:                       # 극이 다르면
            rotate_list.append((i, d*(-1)))
            d *= -1
    # print(rotate_list)

    for rot in rotate_list:
        if rot[1] == -1: #반시계라면
            mat[rot[0]].append(mat[rot[0]].popleft())

        else:
            mat[rot[0]].appendleft(mat[rot[0]].pop())



def moveright(start, direction):
    global mat
    d = direction
    rotate_list = []
    for i in range(start, 4):
        if mat[i - 1][2] == mat[i][6]:  # 왼쪽 바퀴와 i번째 바퀴의 맞닿은 극이 같으면
            break
        else:  # 극이 다르면
            rotate_list.append((i, d * (-1)))
            d *= -1
    # print(rotate_list)

    for rot in rotate_list:
        if rot[1] == -1:  # 반시계라면
            mat[rot[0]].append(mat[rot[0]].popleft())

        else:
            mat[rot[0]].appendleft(mat[rot[0]].pop())



for l in li:
    print(l)
    moveleft(l[0], l[1])
    moveright(l[0], l[1])
    if l[1] == -1:
        mat[l[0]-1].append(mat[l[0]-1].popleft())
    else:
        mat[l[0]-1].appendleft(mat[l[0]-1].pop())

    # print(mat)


total = 0
if mat[0][0] == 0:
    pass
else:
    total+=1

if mat[1][0] == 0:
    pass
else:
    total+=2
if mat[2][0] == 0:
    pass
else:
    total+=4

if mat[3][0] == 0:
    pass
else: total+=8

print(total)



# for s in li:
#     if s[0] == 1:
#         #오른쪽 방향
#         d = s[1]*1
#         for i in range(s[0]-1, 3):
#             if mat[i][2] != mat[i+1][6]: #1번 자석과 2번 자석 극이 다르면
#                 if d == 1: # 시계방향
#                     a = mat[i].pop() #제일 뒤를 뽑아서
#                     mat[i].appendleft(a) #맨앞으로
#                     d = d*-1
#                 elif d == -1: #반시계방향
#                     a = mat[i].popleft() #제일 앞을 뽑아서
#                     mat[i].append(a)    #맨 뒤로
#                     d = d*-1
#
#                 if mat[i+1] == 3: #마지막 톱니
#                     d = d*-1
#                     if d == 1: # 시계방향
#                         a = mat[i+1].pop() #제일 뒤를 뽑아서
#                         mat[i+1].appendleft(a) #맨앞으로
#                     elif d == -1: #반시계방향
#                         a = mat[i+1].popleft() #제일 앞을 뽑아서
#                         mat[i+1].append(a)    #맨 뒤로
#
#             else:
#                 if d == 1: # 시계방향
#                     a = mat[i].pop() #제일 뒤를 뽑아서
#                     mat[i].appendleft(a) #맨앞으로
#                     break
#                 elif d == -1: #반시계방향
#                     a = mat[i].popleft() #제일 앞을 뽑아서
#                     mat[i].append(a)    #맨 뒤로
#                     break
#
#
#
#
#
#     elif s[0] == 2:
#         d = s[1]*1
#         #오른쪽 방향
#         for i in range(s[0]-1, 3):
#             if mat[i][2] != mat[i+1][6]: #2번 자석과 3번 자석 극이 다르면
#                 if d == 1: # 시계방향
#                     a = mat[i].pop() #제일 뒤를 뽑아서
#                     mat[i].appendleft(a) #맨앞으로
#                     d = d*-1
#                 elif d == -1: #반시계방향
#                     a = mat[i].popleft() #제일 앞을 뽑아서
#                     mat[i].append(a)    #맨 뒤로
#                     d = d*-1
#
#                 if mat[i+1] == 3: #마지막 톱니
#                     d = d*-1
#                     if d == 1: # 시계방향
#                         a = mat[i+1].pop() #제일 뒤를 뽑아서
#                         mat[i+1].appendleft(a) #맨앞으로
#                     elif d == -1: #반시계방향
#                         a = mat[i+1].popleft() #제일 앞을 뽑아서
#                         mat[i+1].append(a)    #맨 뒤로
#
#             else:
#                 if d == 1: # 시계방향
#                     a = mat[i].pop() #제일 뒤를 뽑아서
#                     mat[i].appendleft(a) #맨앞으로
#                     break
#                 elif d == -1: #반시계방향
#                     a = mat[i].popleft() #제일 앞을 뽑아서
#                     mat[i].append(a)    #맨 뒤로
#                     break
#
#         #왼쪽 방향
#         if mat[1][6] != mat[0][2]:
#             if d == 1:
#
#
#
#
#     elif s[0] == 3:
#
#     elif s[0] == 4:
#
#

# print(li)









# t_li = []
# for i in range(len(li)):

#     t_li.append((t1[2], t2[6]))
#     t_li.append((t2[2], t3[6]))
#     t_li.append((t3[2], t4[6]))


#     if li[i][0] == 1: # 1번 톱니가 돌 때
#         if t_li[0][0] == t_li[0][1]: #1,2번 톱니가 같은 극이면
#             if li[i][1] == -1:  # 반시계 방향이면
#                 a = t1.popleft()
#                 t1.append(a)

#             elif li[i][1] == 1:  # 시계방향이면
#                 a = t1.pop()
#                 t1.appendleft(a)
#         elif t_li[0][0] != t_li[0][1]: # 1,2번 톱니가 다른 극이면
#             if t_li[1][0] == t_li[1][1]: # 2,3번 톱니가 같은 극이면
#                 if li[i][1] == -1: #반시계 방향이면
#                     a = t1.popleft() #1번은 반시계 2번은 시계방향이동
#                     t1.append(a)
#                     b = t2.pop()
#                     t2.appendleft(b)
#                 elif li[i][1] == 1: # 시계방향이면
#                     a = t1.pop()
#                     t1.appendleft(a)
#                     b = t2.popleft()
#                     t2.append(b)
#             elif t_li[1][0] != t_li[1][1]: #2, 3번 톱니가 다른 극이면
#                 if t_li[2][0] == t_li[2][1]: # 3,4번 톱니가 같은 극이면
#                     if li[i][1] == -1:  # 반시계 방향이면
#                         a = t1.popleft()  # 1번은 반시계 2번은 시계방향이동
#                         t1.append(a)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         c = t3.popleft()
#                         t3.append(c)
#                     elif li[i][1] == 1:  # 시계방향이면
#                         a = t1.pop()
#                         t1.appendleft(a)
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                 elif t_li[2][0] != t_li[2][1]: # 3,4번 톱니가 다른 극이면
#                     if li[i][1] == -1:  # 반시계 방향이면
#                         a = t1.popleft()  # 1번은 반시계 2번은 시계방향이동
#                         t1.append(a)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         c = t3.popleft()
#                         t3.append(c)
#                         d = t4.pop()
#                         t4.appendleft(d)

#                     elif li[i][1] == 1:  # 시계방향이면
#                         a = t1.pop()
#                         t1.appendleft(a)
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         d = t4.popleft()
#                         t4.append(d)

#         print('1', t1,t2,t3,t4)
#     elif li[i][0] == 2: #2번 톱니가 돌때

#         if t_li[0][0] == t_li[0][1]:  # 1,2번 톱니가 같은 극이면
#             if t_li[1][0] == t_li[1][1]: #2,3번 톱니가 같으면
#                 if li[i][1] == -1:  # 2번이 반시계로 돌때
#                     b = t2.popleft()
#                     t2.append(b)

#                 elif li[i][1] == 1:  # 시계방향
#                     b = t2.pop()
#                     t2.append(b)

#             elif t_li[1][0] != t_li[1][1]: #2,3번 톱니가 다르면
#                 if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같으면
#                     if li[i][1] == -1: #2번이 반시계로 돌때
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)

#                     elif li[i][1] == 1: #시계방향
#                         b = t2.pop()
#                         t2.append(b)
#                         c = t3.popleft()
#                         t3.append(c)

#                 elif t_li[2][0] != t_li[2][1]: #3,4 번 톱니가 다르면
#                     if li[i][1] ==  -1: #반시계
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         d = t4.popleft()
#                         t4.append(d)

#                     elif li[i][1] == 1: #시계
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         c = t3.popleft()
#                         t3.append(c)
#                         d = t4.pop()
#                         t4.appendleft(d)


#         elif t_li[0][0] != t_li[0][1]:  # 1,2번 톱니가 다른 극이면

#             if t_li[1][0] == t_li[1][1]: #2,3번 톱니가 같으면

#                 if li[i][1] == -1:  # 2번이 반시계로 돌때
#                     b = t2.popleft() ##################################################################3
#                     t2.append(b)
#                     a = t1.pop()
#                     t1.appendleft(a)

#                 elif li[i][1] == 1: #시계 방향
#                     b = t2.pop()
#                     t2.appendleft(b)
#                     a = t1.popleft()
#                     t1.append(a)

#             elif t_li[1][0] != t_li[1][1]: #2,3번 톱니가 다르면

#                 if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같으면

#                     if li[i][1] == -1: #2번이 반시계로 돌때
#                         a = t1.pop()
#                         t1.appendleft(a)
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)

#                     elif li[i][1] == 1: #시계방향
#                         a = t1.popleft()
#                         t1.append(a)
#                         b = t2.pop()
#                         t2.append(b)
#                         c = t3.popleft()
#                         t3.append(c)

#                 elif t_li[2][0] != t_li[2][1]: #3,4 번 톱니가 다르면

#                     if li[i][1] ==  -1: #반시계
#                         a = t1.pop()
#                         t1.appendleft(a)
#                         b = t2.popleft()
#                         t2.append(b)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         d = t4.popleft()
#                         t4.append(d)

#                     elif li[i][1] == 1: #시계
#                         a = t1.popleft()
#                         t1.append(a)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         c = t3.popleft()
#                         t3.append(c)
#                         d = t4.pop()
#                         t4.appendleft(d)


#         print('2',t1,t2,t3,t4)

#     elif li[i][0] == 3: #3번 톱니가 돌 때
#         if t_li[2][0] == t_li[2][1]:  # 3,4번 톱니가 같은 극이면
#             if t_li[1][0] == t_li[1][1]:  # 2,3번 톱니가 같으면
#                 if li[i][1] == -1:  # 3번이 반시계로 돌때
#                     c = t3.popleft()
#                     t3.append(c)

#                 elif li[i][1] == 1:  # 시계방향
#                     c = t3.pop()
#                     t3.append(c)

#             elif t_li[1][0] != t_li[1][1]:  # 2,3번 톱니가 다르면
#                 if t_li[0][0] == t_li[0][1]:  # 1,2번 톱니가 같으면
#                     if li[i][1] == -1:  # 3번이 반시계로 돌때
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                     elif li[i][1] == 1:  # 시계방향
#                         c = t3.pop()
#                         t3.append(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                 elif t_li[2][0] != t_li[2][1]:  # 1,2 번 톱니가 다르면
#                     if li[i][1] == -1:  # 반시계
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         a = t1.popleft()
#                         t1.append(a)
#                     elif li[i][1] == 1:  # 시계
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                         a = t1.pop()
#                         t1.appendleft(a)

#         elif t_li[2][0] != t_li[2][1]:  # 3,4번 톱니가 다른 극이면
#             if t_li[1][0] == t_li[1][1]:  # 2,3번 톱니가 같으면
#                 if li[i][1] == -1:  # 3번이 반시계로 돌때
#                     d = t4.pop()
#                     t4.appendleft(d)
#                     c = t3.popleft()
#                     t3.append(c)
#                 elif li[i][1] == 1:  # 시계 방향
#                     d = t4.popleft()
#                     t4.append(d)
#                     c = t3.pop()
#                     t3.appendleft(c)
#             elif t_li[1][0] != t_li[1][1]:  # 2,3번 톱니가 다르면
#                 if t_li[2][0] == t_li[2][1]:  # 1,2번 톱니가 같으면
#                     if li[i][1] == -1:  # 3번이 반시계로 돌때
#                         d = t4.pop()
#                         t4.appendleft(d)
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                     elif li[i][1] == 1:  # 시계방향
#                         d = t4.popleft()
#                         t4.append(d)
#                         c = t3.pop()
#                         t3.append(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                 elif t_li[2][0] != t_li[2][1]:  # 1,2 번 톱니가 다르면
#                     if li[i][1] == -1:  # 반시계
#                         d = t4.pop()
#                         t4.appendleft(d)
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         a = t1.popleft()
#                         t1.append(a)
#                     elif li[i][1] == 1:  # 시계
#                         d = t4.popleft()
#                         t4.append(d)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                         a = t1.pop()
#                         t1.appendleft(a)
#         print('3',t1,t2,t3,t4)

#     elif li[i][0] == 4: # 4번 톱니가 돌 때
#         if t_li[2][0] == t_li[2][1]: #3,4번 톱니가 같은 극이면
#             if li[i][1] == -1:  # 반시계 방향이면
#                 d = t4.popleft()  # 4번은 반시계 3번은 시계방향이동
#                 t4.append(d)

#             elif li[i][1] == 1:  # 시계방향이면
#                 d = t4.pop()
#                 t4.appendleft(d)

#         elif t_li[2][0] != t_li[2][1]: # 3,4번 톱니가 다른 극이면
#             if t_li[1][0] == t_li[1][1]: # 2,3번 톱니가 같은 극이면
#                 if li[i][1] == -1: #반시계 방향이면
#                     d = t4.popleft() #4번은 반시계 3번은 시계방향이동
#                     t4.append(d)
#                     c = t3.pop()
#                     t3.appendleft(c)
#                 elif li[i][1] == 1: # 시계방향이면
#                     d = t4.pop()
#                     t4.appendleft(d)
#                     c = t3.popleft()
#                     t3.append(c)
#             elif t_li[1][0] != t_li[1][1]: #2, 3번 톱니가 다른 극이면
#                 if t_li[0][0] == t_li[0][1]: # 1,2번 톱니가 같은 극이면
#                     if li[i][1] == -1:  # 반시계 방향이면
#                         d = t4.popleft()  # 1번은 반시계 2번은 시계방향이동
#                         t4.append(d)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                     elif li[i][1] == 1:  # 시계방향이면
#                         d = t4.pop()
#                         t4.appendleft(d)
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                 elif t_li[0][0] != t_li[0][1]: # 1,2번 톱니가 다른 극이면
#                     if li[i][1] == -1:  # 반시계 방향이면
#                         d = t4.popleft()  # 1번은 반시계 2번은 시계방향이동
#                         t4.append(d)
#                         c = t3.pop()
#                         t3.appendleft(c)
#                         b = t2.popleft()
#                         t2.append(b)
#                         a = t1.pop()
#                         t1.appendleft(a)
#                     elif li[i][1] == 1:  # 시계방향이면
#                         d = t4.pop()
#                         t4.appendleft(d)
#                         c = t3.popleft()
#                         t3.append(c)
#                         b = t2.pop()
#                         t2.appendleft(b)
#                         a= t1.popleft()
#                         t1.append(a)
#         print('4',t1,t2,t3,t4)
#     t_li.clear()

# print(t1)
# print(t2)

# total = 0
# if t1[0] == 0:
#     pass
# elif t1[1] == 1:
#     total+=1
#
# if t2[0] == 0:
#     pass
# else:
#     total+=2
# if t3[0] == 0:
#     pass
# else:
#     total+=4
#
# if t4[0] == 0:
#     pass
# else: total+=8

# print(total)
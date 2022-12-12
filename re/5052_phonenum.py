# import sys
#
# lines = sys.stdin.readlines()
# for line in lines:
#     A, B = map(int, line.split())
#     print(A+B)
import sys

# a = sys.stdin.readline


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    flag = False

    num_list = [sys.stdin.readline().rstrip() for _ in range(n)]

    # print(num_list)

    num_list.sort()
    # print(num_list)

    # num_set = set(num_list)

    for i in range(n-1):
        # for j in range(i+1, len(num_list)):
        if num_list[i] in num_list[i+1][:len(num_list[i])]:
            flag = True
            break
        # if flag == False:
        #     break

    if flag:
        print('N0')
    else:
        print('YES')






    # for i in range(n):
    #     num = list(sys.stdin.readline().rstrip())
    #
    #     # print(num)
    #     num_str = ''
    #     for j in range(len(num)):
    #         num_str += num[j]
    #         # print(num_str)
    #         if num_str in num_set:
    #             flag = False
    #             break
    #     if flag == False:
    #         break
    #
    #     num_set.add(num_str)
    # # print(num_set)
    # if flag == False:
    #     print('N0')
    # if flag == True:
    #     print('YES')



# def solution(cap, n, deliveries, pickups):
#     totalD = 0
#     while sum(deliveries) != 0 or sum(pickups) != 0:
#         d = 0
#         p = 0
#         longD = False
#         longP = False
#         dist = 0
#         # print(deliveries)
#         # print(pickups)
#         for i in range(len(deliveries)-1, -1, -1):
#
#             if deliveries[i] and not longD:
#                 longD = True
#                 dist = max(dist, i+1)
#
#                 while d != cap and deliveries[i] != 0:
#                     deliveries[i] -= 1
#                     d += 1
#
#
#                 if d == cap and deliveries[i] == 0:
#                     deliveries = deliveries[:i]
#                     break
#
#                 elif d == cap:
#                     deliveries = deliveries[:i+1]
#                     break
#
#             elif deliveries[i] and longD and d != cap:
#                 while d != cap and deliveries[i] != 0:
#                     deliveries[i] -= 1
#                     d += 1
#
#                 if d == cap and deliveries[i] == 0:
#                     deliveries = deliveries[:i]
#                     break
#
#                 elif d == cap:
#                     deliveries = deliveries[:i+1]
#                     break
#
#         for j in range(len(pickups)-1, -1, -1):
#             if pickups[j] and not longP:
#                 longP = True
#                 dist = max(dist, j+1)
#
#                 while p != cap and pickups[j] != 0:
#                     pickups[j] -= 1
#                     p += 1
#
#                 if p == cap and pickups[j] == 0:
#                     pickups = pickups[:j]
#                     break
#
#                 elif p == cap:
#                     pickups = pickups[:j+1]
#                     break
#
#             elif pickups[j] and longP and p != cap:
#                 while p != cap and pickups[j] != 0:
#                     pickups[j] -= 1
#                     p += 1
#
#                 if p == cap and pickups[j] == 0:
#                     pickups = pickups[:j]
#                     break
#
#                 elif p == cap:
#                     pickups = pickups[:j+1]
#                     break
#
#
#         totalD += dist*2
#
#     answer = totalD
#     return answer


def solution(cap, n, deliveries, pickups):

    # 일단 배달과 수거 cap을 따로 나눠서 생각함
    # cap = 4라면, 배달 cap도 4이고 수거 cap도 4라고 생각하고 풀기

    d, p = n-1, n-1 # d는 배달 인덱스, p는 수거 인덱스
    answer = 0

    #d와 p를 하나씩 줄이면서 d, p가 둘 다 0이 될 때까지 돌아
    while d > -1 or p > -1:

                        # 물류창고에서 출발
        longD = False   # 배달할 가장 먼 집을 방문한다면 true로 바꿈
        longP = False   # 수거할 가장 먼 집을 방문한다면 true로 바꿈
        dcap = cap      # 배달할 할당량, 관념적으로 배달할 물건을 최대로 싣는다고 가정
        pcap = cap      # 수거할 할당량, 관념적으로 수거할 물건을 최대로 싣는다고 가정
        dist = 0        # 물류창고에서부터 (배달이나 수거할 집)까지의 최대 거리

        #여기부터 배달 먼저 ################################################################3
        while dcap and d > -1:              # 배달 cap이 남아있고 인덱스가 -1보다 크면
            if deliveries[d] and not longD:     # 배달할 것이 있고 가장 먼 곳이라면
                longD = True                        # longD를 true로 바꾸고
                dist = max(d+1, dist)               # 거리를 잼

                if deliveries[d] > dcap:            # 해당 집의 배달 양이 cap을 초과하면
                    deliveries[d] -= dcap
                    dcap = 0

                else:                               # 해당 집의 배달 양이 cap보다 작거나 같으면
                    dcap -= deliveries[d]
                    deliveries[d] = 0
                    d -= 1                          # 한 칸 왼쪽 집으로 이동

            elif deliveries[d] and longD:       # 배달할 것이 있는데 물류창고로부터 가장 먼 곳을 이미 방문했다면
                if deliveries[d] > dcap:            #
                    deliveries[d] -= dcap           #
                    dcap = 0                        #
                                                    # 위와 같음
                else:                               #
                    dcap -= deliveries[d]           #
                    deliveries[d] = 0               #
                    d -= 1                          #
            else:                               # 배달할 것이 없으면 즉 0 이라면
                d -= 1                              # 그냥 한칸 이동
            ##############################################################################33

        # 여기부터는 수거인데 배달과 로직이 같음##################################################
        while pcap and p > -1:
            if pickups[p] and not longP:
                longP = True
                dist = max(p+1, dist)

                if pickups[p] > pcap:
                    pickups[p] -= pcap
                    pcap = 0


                else:
                    pcap -= pickups[p]
                    pickups[p] = 0
                    p -= 1


            elif pickups[p] and longP:
                if pickups[p] > pcap:
                    pickups[p] -= pcap
                    pcap = 0
                else:
                    pcap -= pickups[p]
                    pickups[p] = 0
                    p -= 1
            else:
                p -= 1
        ###################################################################################33

        answer += dist * 2 # 배달과 수거 중 더 멀리 간 거리의 왕복 값을 answer에 더해줌

    return answer



print(solution(4, 5, [0,0,0,0,0], [0,3,0,4,0]))
# print(solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))


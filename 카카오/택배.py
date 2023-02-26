# def solution(cap, n, deliveries, pickups):
#     totalD = 0
#     while sum(deliveries) != 0 and sum(pickups) != 0:
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

    d, p = n-1, n-1
    answer = 0
    while d > -1 and p > -1:
        longD = False
        longP = False
        dcap = cap
        pcap = cap
        dist = 0
        while dcap and d > -1:
            if deliveries[d] and not longD:
                longD = True
                dist = max(d+1, dist)

                if deliveries[d] > dcap:
                    deliveries[d] -= dcap
                    dcap = 0

                else:
                    dcap -= deliveries[d]
                    deliveries[d] = 0
                    d -= 1

            elif deliveries[d] and longD:
                if deliveries[d] > dcap:
                    deliveries[d] -= dcap
                    dcap = 0

                else:
                    dcap -= deliveries[d]
                    deliveries[d] = 0
                    d -= 1
            else:
                d -= 1

        while pcap and p > -1:
            print(p)
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

        answer += dist * 2

    return answer



print(solution(4, 5, [0,0,0,0,0], [0,3,0,4,0]))
# print(solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))


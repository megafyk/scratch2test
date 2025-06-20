class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1 heap
        # time O(mlogm + nlogn), O(n)
        meetings = sorted(meetings)
        avail = []
        cnt = [0] * n
        for i in range(n): 
            heappush(avail, (0, i))
        
        for s,e in meetings:
            while avail and avail[0][0] < s:
                _,room = heappop(avail)
                heappush(avail, (s,room))

            end,room = heappop(avail)
            heappush(avail, (end + (e-s), room))
            cnt[room] += 1

        return cnt.index(max(cnt))



# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         # 2 heaps
#         # time O(mlogm + m*logn), space O(n)
#         meetings = sorted(meetings)

#         avail = [i for i in range(n)]
#         used = []
#         cnt = [0] * n

#         for s, e in meetings:
#             while used and used[0][0] <= s:
#                 _, room = heappop(used)
#                 heappush(avail, room)
            
#             if not avail:
#                 end, room = heappop(used)
#                 e = end + (e - s)
#                 heappush(avail, room)
            
#             room = heappop(avail)
#             cnt[room] += 1
#             heappush(used, (e, room))

        return cnt.index(max(cnt))
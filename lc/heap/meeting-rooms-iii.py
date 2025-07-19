class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap
        # time O(mlogm + m*logn), space O(n)
        m = len(meetings)
        meetings.sort()
        avail = [(0, i) for i in range(n)]  # (time_can_start, room)
        cnt_room = [0] * n
        for s, e in meetings:
            while avail and avail[0][0] < s:
                _, room = heappop(avail)
                heappush(avail, (s, room))
            end, room = heappop(avail)  # skip to end if no room avail or get avail
            heappush(avail, (end + e - s, room))
            cnt_room[room] += 1

        return cnt_room.index(max(cnt_room))


class Solution2:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 2 heaps
        # time O(mlogm + m*logn), space O(n)
        meetings = sorted(meetings)

        avail = [i for i in range(n)]
        used = []
        cnt = [0] * n

        for s, e in meetings:
            while used and used[0][0] <= s:
                _, room = heappop(used)
                heappush(avail, room)

            if not avail:
                end, room = heappop(used)
                e = end + (e - s)
                heappush(avail, room)

            room = heappop(avail)
            cnt[room] += 1
            heappush(used, (e, room))

        return cnt.index(max(cnt))


class Solution3:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # naive solution -> tle
        m = len(meetings)
        meetings.sort()  # sort by start time

        avail = [i for i in range(n)]
        serve = []
        cnt_serve = [0] * n

        cur_meet = 0
        time = 0
        while True:  # tle
            if cur_meet == m:  # no meeting left
                break

            while serve and serve[0][0] <= time:
                _, room = heappop(serve)
                heappush(avail, room)

            while avail and cur_meet < m and meetings[cur_meet][0] <= time:
                room = heappop(avail)
                heappush(
                    serve, (time + meetings[cur_meet][1] - meetings[cur_meet][0], room)
                )
                cur_meet += 1
                cnt_serve[room] += 1

            time += 1

        mx_room = -1
        mx_cnt = -1
        for i in range(n):
            if cnt_serve[i] > mx_cnt:
                mx_room = i
                mx_cnt = cnt_serve[i]
        return mx_room

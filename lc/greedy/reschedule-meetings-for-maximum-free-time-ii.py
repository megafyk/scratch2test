class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # greedy
        # time O(n), space O(n)
        n = len(startTime)
        gaps = [startTime[0]]

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        mx_right = [0] * len(gaps)
        for i in range(len(gaps) - 2, -1, -1):
            mx_right[i] = max(mx_right[i + 1], gaps[i + 1])


        mx_left = 0
        mx_free = 0
        for i in range(1, len(gaps)):
            t = gaps[i] + gaps[i - 1]
            idx = i - 1
            
            e = endTime[idx] - startTime[idx]
            if e <= mx_left or e <= mx_right[i]:
                t += e
            
            mx_free = max(mx_free, t)
            mx_left = max(gaps[i - 1], mx_left)
        return mx_free


class Solution1:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # sorting + greedy
        # time O(nlogn), space O(n)
        n = len(startTime)
        gaps = [startTime[0]]
        avail = [(startTime[0], 0)]
        for i in range(1, n):
            gap = startTime[i] - endTime[i - 1]
            gaps.append(gap)
            bisect.insort(avail, (gap, i))
        gaps.append(eventTime - endTime[-1])
        bisect.insort(avail, (eventTime - endTime[-1], n))
        mx_free = 0
        for i in range(1, len(gaps)):
            t = gaps[i] + gaps[i - 1]
            idx = i - 1
            e = endTime[idx] - startTime[idx]
            for i in range(len(avail) - 1, -1, -1):
                if avail[i][0] < e:
                    break
                if avail[i][0] >= e and avail[i][1] != idx + 1 and avail[i][1] != idx:
                    t += e
                    break

            mx_free = max(mx_free, t)
        return mx_free

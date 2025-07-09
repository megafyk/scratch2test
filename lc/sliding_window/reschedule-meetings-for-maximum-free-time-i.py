class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # sliding window
        # time O(n), space O(1)
        n = len(startTime)
        gaps = [startTime[0]]
        # preprocess gap
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        max_free = cur_free = sum(gaps[:k+1])
        for i in range(k+1, len(gaps)):
            cur_free += (gaps[i] - gaps[i-k-1])
            max_free = max(max_free, cur_free)
        return max_free
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import bisect

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # sorting + greedy
        # time O(nlogn), space O(n)
        start = []
        end = []
        for interval in intervals:
            bisect.insort(start, interval.start)
            bisect.insort(end, interval.end)

        res = 0
        cur_room = 0
        n = len(intervals)
        i = j = 0
        while i < n:
            if start[i] < end[j]:
                i += 1
                cur_room += 1
                res = max(res, cur_room)
            else:
                j += 1
                cur_room -= 1
        return res
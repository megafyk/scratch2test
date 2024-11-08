from typing import List


class Solution:
    def test(self, mask, i):
        return (mask >> i) & 1 == 1

    def check_subset(self, n, requests, mask):
        cnt = [0 for i in range(n)]
        for i, (fr, to) in enumerate(requests):
            if self.test(mask, i):
                cnt[fr] += 1
                cnt[to] -= 1
        return max(cnt) == 0

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        res = 0
        # regconize a valid pattern (subset/mask) is a cycle. eg: [0,1],[1,0],[0,1],[1,2],[2,0] is 0 -> 1 -> 0 -> 1 -> 2 -> 0 (back to 0)
        # problem turn into find subset with max number of 1 bit

        '''
        The idea is to use a bitmask to represent a subset of transfer requests. 
        Each bit in the bitmask corresponds to a transfer request in the original array. 
        A 1 at a particular bit position indicates that the corresponding transfer request is included in the current subset, and a 0 indicates it's excluded.

        We can iterate through all possible bitmasks (using a loop from 0 to 2^n - 1, where n is the number of requests) 
        and check if the corresponding subset of requests is achievable.
        A subset is achievable if the net change in the number of employees for each building is zero.
        '''
        for mask in range(1<<m):
            if self.check_subset(n, requests, mask):
                res = max(res, mask.bit_count())
        return res
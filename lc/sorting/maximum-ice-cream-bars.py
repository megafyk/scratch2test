class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # greedy + sort
        # time O(nlogn), space O(1)
        costs.sort()
        res = 0
        for c in costs:
            if c > coins:
                break
            coins -= c
            res += 1
        return res


class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # counting sort
        # time O(n), space O(n)
        cnt = defaultdict(int)
        mx_cost = 0
        for c in costs:
            cnt[c] += 1
            if mx_cost < c:
                mx_cost = c
        res = 0
        for c in range(1, mx_cost + 1):
            if cnt[c] == 0:
                continue
            if cnt[c] * c > coins:
                res += coins // c
                break
            else:
                coins -= c * cnt[c]
                res += cnt[c]
        return res

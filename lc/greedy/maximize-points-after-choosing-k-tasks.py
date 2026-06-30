class Solution:
    def maxPoints(self, tech1: List[int], tech2: List[int], k: int) -> int:
        # greedy + sort
        # time O(nlogn), space O(n)
        n = len(tech1)
        arr = [((tech1[i] - tech2[i]), tech1[i], tech2[i]) for i in range(n)]
        arr.sort(reverse=True)
        res = 0
        for i in range(n):
            _, t1, t2 = arr[i]
            if k > 0:
                res += t1
                k -= 1
            else:
                res += max(t1, t2)
        return res

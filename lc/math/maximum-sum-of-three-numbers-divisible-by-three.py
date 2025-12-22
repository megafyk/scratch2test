class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        remain = defaultdict(list)
        for num in nums:
            remain[num%3].append(num)
        res = 0
        if len(remain[2]) >= 3:
            arr = remain[2]
            res = max(res, arr[-1] + arr[-2] + arr[-3])
        if len(remain[1]) >= 3:
            arr = remain[1]
            res = max(res, arr[-1] + arr[-2] + arr[-3])
        if len(remain[0]) >= 3:
            arr = remain[0]
            res = max(res, arr[-1] + arr[-2] + arr[-3])
        if len(remain[2]) >= 1 and len(remain[1]) >= 1 and len(remain[0]) >= 1:
            res = max(res, remain[2][-1] + remain[1][-1] + remain[0][-1])
        return res
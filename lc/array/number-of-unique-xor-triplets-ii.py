class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        pairs = set()
        for i in range(n):
            for j in range(n):
                pairs.add(nums[i] ^ nums[j])
        res = set()
        for i in range(n):
            for p in pairs:
                res.add(nums[i] ^ p)
        return len(res)

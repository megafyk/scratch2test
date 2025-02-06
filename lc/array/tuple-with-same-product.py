class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # space 
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                cnt[nums[i] * nums[j]] += 1
        res = 0
        for k,v in cnt.items():
            res += 8 * (v * (v-1) // 2)
        return res 

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # sliding window
        # time O(n), time O(1)
        n = len(nums)
        cur_sum = 0
        i = 0
        hm = {}
        mx = 0
        for j in range(n):
            cur_sum += nums[j]

            while nums[j] in hm:
                cur_sum -= nums[i]
                del hm[nums[i]]
                i += 1

            hm[nums[j]] = j

            if j - i + 1 > k:
                cur_sum -= nums[i]
                del hm[nums[i]]
                i += 1
            if j-i+1 == k:
                mx = max(mx, cur_sum)
        return mx

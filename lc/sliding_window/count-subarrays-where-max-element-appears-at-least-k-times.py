class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window
        # time O(N), space O(1)
        N = len(nums)
        mx = max(nums)
        res = 0
        cnt = 0
        i = 0

        for j in range(N):
            cnt += 1 if nums[j] == mx else 0
            while i <= j and cnt >= k:
                if nums[i] == mx:
                    cnt -= 1
                i += 1
            res += i
        return res
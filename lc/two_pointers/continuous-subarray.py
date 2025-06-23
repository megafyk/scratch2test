class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # 2 pointers
        # time O(n), space O(1)
        n = len(nums)
        mx = mi = nums[0]
        i = 0
        res = 0
        for j in range(n):
            mx = max(mx, nums[j])
            mi = min(mi, nums[j])
            if mx - mi > 2:
                win = j - i
                res += win*(win+1) // 2
                i = j
                mx = mi = nums[j]
                while i > 0 and abs(nums[j] - nums[i-1]) <= 2:
                    i -= 1
                    mx = max(mx , nums[i])
                    mi = min(mi , nums[i])

                if i < j:
                    win = j - i
                    res -= win*(win+1) // 2
        win = j - i + 1
        res += ((win*(win+1)) // 2)
        return res

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        n = len(nums)
        i = 0

        for j in range(1, n):
            if nums[j] - nums[j-1] > 1:
                if j-1 != i:
                    res.append(f"{nums[i]}->{nums[j-1]}")
                else:
                    res.append(f"{nums[i]}")
                i = j
        if nums[i] == nums[-1]:
            res.append(f"{nums[i]}")
        else:
            res.append(f"{nums[i]}->{nums[j]}")

        return res
        
                
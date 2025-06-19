class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        # sorting + greedy
        # time O(nlogn), space O(1)

        n = len(nums)
        nums = sorted(nums)
        cnt = 1
        j = 1
        mi = nums[0]
        for j in range(1, n):
            if nums[j] - mi > k:
                cnt += 1
                mi = nums[j]

        return cnt
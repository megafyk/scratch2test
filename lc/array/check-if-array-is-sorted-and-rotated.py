class Solution:
    def check(self, nums: List[int]) -> bool:
        # array rotate
        # time O(N), space O(1)
        N = len(nums)
        cnt = 1
        for i in range(1, N * 2):
            if nums[(i-1) % N] <= nums[i%N]:
                cnt += 1
            else:
                cnt = 1
            if cnt == N:
                return True
        return False

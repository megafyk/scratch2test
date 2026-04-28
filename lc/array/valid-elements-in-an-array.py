class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            if i == 0 or i == n - 1:
                arr.append(nums[i])
            else:
                valid_r = True
                for r in range(i + 1, n):
                    if nums[r] >= nums[i]:
                        valid_r = False
                        break
                valid_l = True
                for l in range(i - 1, -1, -1):
                    if nums[l] >= nums[i]:
                        valid_l = False
                        break
                if valid_r or valid_l:
                    arr.append(nums[i])
        return arr

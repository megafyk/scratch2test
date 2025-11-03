class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # sorting
        # time O(n), space O(1)
        n = len(nums)
        nums.sort()
        prev = -sys.maxsize
        res = 0
        for i in range(n):
            cur = min(max(prev+1, nums[i]-k), nums[i]+k)
            if cur > prev:
                res += 1
                prev = cur
        return res

class Solution1:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # binary search
        # time O(nlogn + nlogk), space O(1)
        n = len(nums)
        nums.sort()
        prev = -sys.maxsize
        res = 0
        for i in range(n):
            l,r = -k,k
            while l < r:
                mid = (l+r) // 2
                if nums[i] + mid > prev:
                    r = mid
                else:
                    l = mid + 1
            if -k<=l<=k and nums[i] + l > prev:
                prev = nums[i] + l
                res += 1
        return res
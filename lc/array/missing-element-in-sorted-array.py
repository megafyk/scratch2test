class Solution:
    """
    @param nums: An integer array
    @param k: An integer
    @return: Missing positive number in sorted array
    """
    def find_positive(self, nums: List[int], k: int) -> int:
        #
        n = len(nums)
        pass

class Solution1:
    """
    @param nums: An integer array
    @param k: An integer
    @return: Missing positive number in sorted array
    """
    def find_positive(self, nums: List[int], k: int) -> int:
        # write your code here
        # https://www.lintcode.com/problem/3884
        s = set(nums)
        cur = 1
        while k > 0:
            if cur not in s:
                k -= 1
            cur += 1
        return cur-1

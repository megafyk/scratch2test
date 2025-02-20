class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # time O(2^n), space O(n)
        n = len(nums)
        def backtrack(cur):
            if len(cur) == n:
                if cur not in nums:
                    return cur
                return ""
            
            res = backtrack(cur+"0")

            if not res:
                return backtrack(cur+"1")
            return res
        return backtrack("") 

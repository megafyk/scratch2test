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

class Solution1:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(1<<(n)):
            t = bin(i)[2:]
            t = t + "0" * (n-len(t))
            if t not in nums:
                return t
        return ""

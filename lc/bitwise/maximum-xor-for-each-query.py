class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # bitwise
        # time O(n), space O(n)
        ans =  []
        mx = 2 ** maximumBit - 1
        cur = 0
        for num in nums:
            cur ^= num
            k = mx ^ cur
            ans.append(k)
        return ans[::-1]

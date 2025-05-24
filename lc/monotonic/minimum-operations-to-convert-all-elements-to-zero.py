class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # increase monotonic stack
        # time O(n), space O(n)
        
        st = []
        res = 0
        for num in nums:
            if num == 0: continue
            while st and st[-1] > num:
                st.pop()
            if not st or st[-1] < num: # if num > last num => need 1 operation to clear num
                res += 1
                st.append(num)

        return res
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # greedy
        # time O(n), space O(1)
        t = nums[0] % 2
        all_odd = all_even = both = 0
        for num in nums:
            if num % 2 == 0:
                all_even +=1
            else:
                all_odd += 1
            
            if num % 2 == t:
                both += 1
                t ^= 1 # toggle
        return max(both, all_odd, all_even)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # bitwise
        # time O(n) space O(1)
        first_bit = 0 # suppose first bit in 0, can set 1 no matter
        cur_bit = first_bit
        for b in derived:
            if b == 1: # prev bit must diff else keep cur_bit
                cur_bit ^= 1
        return cur_bit == first_bit # contradiction

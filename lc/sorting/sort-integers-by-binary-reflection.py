class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def helper(a, b):
            bin_a = bin(a)[2:][::-1]
            bin_b = bin(b)[2:][::-1]
            nw_a = int(bin_a, 2)
            nw_b = int(bin_b, 2)
            
            if nw_a == nw_b: return 1 if a > b else -1
            return 1 if nw_a > nw_b else -1

        nums.sort(key=cmp_to_key(helper))
        return nums
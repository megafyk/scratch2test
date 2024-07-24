class Solution:

    def mapped(self, a, mapping):
        newa = 0
        for c in str(a):
            newa = newa * 10 + mapping[int(c)]
        return newa

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # complexity: time O(nlogn), mem O(n)
        tmp = []
        for idx, n in enumerate(nums):
            tmp.append((self.mapped(n, mapping), idx))
        tmp = sorted(tmp)
        return [nums[idx] for _, idx in tmp]

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # binary search
        # time O(nlogn), space O(n)
        n = len(spells)
        m = len(potions)
        potions.sort()

        def count(spell):
            l,r = 0, m
            while l < r:
                mid = (l+r) // 2
                if spell * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            if l == m: return 0
            return m-l

        res = [0] * n

        for i in range(n):
            res[i] = count(spells[i])
        return res
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # array
        # time O(n), space O(1)
        n = len(skill)
        summ = sum(skill)
        if summ % (n//2) != 0: return -1
        target = summ // (n//2)
        cnt = [0] * 1001
        
        product = 0

        for s1 in skill:
            if cnt[target - s1]:
                cnt[target-s1] -= 1
                product += s1 * (target-s1)
            else:
                cnt[s1] += 1

        return product if sum(cnt) == 0 else -1

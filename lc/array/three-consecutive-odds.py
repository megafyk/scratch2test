class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # array
        # time O(N), space O(1)
        cnt = 0
        for n in arr:
            if n % 2 == 0:
                cnt = 0
            else:
                cnt += 1
                if cnt >= 3:
                    return True
        return False
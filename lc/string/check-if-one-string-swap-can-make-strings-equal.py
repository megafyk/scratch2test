class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # string
        # time O(n), space O(1)
        idx1 = idx2 = 0
        n = len(s1)
        cnt_diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                cnt_diff += 1
                if cnt_diff > 2:
                    return False
                elif cnt_diff == 1:
                    idx1 = i
                else:
                    idx2 = i
        return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]

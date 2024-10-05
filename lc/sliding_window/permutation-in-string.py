class Solution:
    def idx(self, c):
        return ord(c) - ord("a")

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # time O(26*n), space O(n)
        if len(s1) > len(s2): return False
        cnt_s1 = [0] * 26
        cnt_s2 = [0] * 26

        for i in range(len(s1)):
            cnt_s1[self.idx(s1[i])] += 1
            cnt_s2[self.idx(s2[i])] += 1

        i, j = 0, len(s1) - 1

        while j < len(s2):
            if cnt_s1 == cnt_s2:
                return True
            cnt_s2[self.idx(s2[i])] -= 1
            i+=1
            j+=1
            if j < len(s2):
                cnt_s2[self.idx(s2[j])] += 1
        return False

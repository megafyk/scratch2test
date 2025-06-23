class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # two pointers
        # time O(n), space O(1)
        m = len(str1)
        n = len(str2)
        j = 0
        for i in range(m):
            if j == n:
                return True
            if ord(str1[i]) == ord(str2[j]) or ord(str1[i]) + 1  == ord(str2[j]) or (str1[i] == "z" and str2[j] == "a"):
                j += 1

        return j == n

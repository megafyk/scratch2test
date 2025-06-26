class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedy
        # time O(n), space O(1)
        n = len(s)
        count = 0
        total = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                count += 1
            else:
                if (1 << count) > k:
                    continue
                if (total + (1 << count)) <= k:
                    total += (1 << count)
                    count += 1
        return count

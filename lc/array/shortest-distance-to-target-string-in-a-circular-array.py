class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # array
        # m = len(words), n = len(target)
        # time O(m*n), space O(1)
        if words[startIndex] == target:
            return 0
        n = len(words)
        mi = inf
        for k in range(1, n):
            if words[(startIndex+k+n) % n] == target or words[(startIndex-k+n) % n] == target:
                mi = min(mi, k)
                break
        return -1 if mi == inf else mi
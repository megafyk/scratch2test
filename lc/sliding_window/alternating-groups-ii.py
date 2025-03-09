class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # sliding windows
        # time O(n+k), space O(k)
        i,j = 0,0
        colors.extend(colors[:k-1])
        res = 0
        diff = False
        for j in range(len(colors)):
            if j > 0:
                diff = colors[j] != colors[j-1]
            if not diff:
                i = j
            if j-i == k-1:
                res += 1
                i += 1
            else:
                j += 1
        return res
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = {k:0 for k in range(1, n**2+1)}
        for i in range(n):
            for j in range(n):
                cnt[grid[i][j]] += 1
        res = [-1, -1]
        for k,v in cnt.items():
            if v == 0: res[1] = k
            if v == 2: res[0] = k
        return res
        
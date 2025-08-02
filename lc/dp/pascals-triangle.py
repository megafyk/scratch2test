class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # dp
        # time O(n^2), space O(n)
        if numRows == 1: return [[1]]
        res = [[1], [1,1]]    
        for _ in range(2, numRows):
            nw_row = [1]
            prev = res[-1]
            for j in range(1, len(prev)):
                nw_row.append(prev[j-1] + prev[j])
            nw_row.append(1)
            res.append(nw_row)
        return res
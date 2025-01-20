class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # hashtable + counting
        # time O(m*n + k), space O(m*n)
        m = len(mat)
        n = len(mat[0])
        cnt_row = [0] * m
        cnt_col = [0] * n
        hm = {}
        for r in range(m):
            for c in range(n):
                hm[mat[r][c]] = (r,c)
        k = len(arr)
        for idx,num in enumerate(arr):
            r,c = hm[num]
            cnt_row[r] += 1
            cnt_col[c] += 1
            
            if cnt_row[r] == n: return idx 
            if cnt_col[c] == m: return idx

        return 0
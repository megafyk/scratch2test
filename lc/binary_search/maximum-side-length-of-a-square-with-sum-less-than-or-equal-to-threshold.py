class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix matrix
        # time O(m*n), space O(1)
        m = len(mat)
        n = len(mat[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    mat[i][j] += mat[i-1][j]
                if j > 0:
                    mat[i][j] += mat[i][j-1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i-1][j-1]
                for l in range(res, min(i,j) + 2):
                    s = 0
                    if i - l >= 0:
                        s += mat[i-l][j]
                    if j - l >= 0:
                        s += mat[i][j-l]
                    if i-l >= 0 and j-l >= 0:
                        s -= mat[i-l][j-l]          
                    if mat[i][j] - s <= threshold:
                        res = max(res, l)
                    else:
                        break
        return res

class Solution1:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix matrix
        # time O(m*n*log(min(m,n))), space O(1)
        m = len(mat)
        n = len(mat[0])
        res = 0

        def check(i, j, length):
            s = 0
            if i - length >= 0:
                s += mat[i-length][j]
            if j - length >= 0:
                s += mat[i][j-length]
            if i-length >= 0 and j-length >= 0:
                s -= mat[i-length][j-length]

            return (mat[i][j] - s) <= threshold

        for i in range(m):
            for j in range(n):
                if i > 0:
                    mat[i][j] += mat[i-1][j]
                if j > 0:
                    mat[i][j] += mat[i][j-1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i-1][j-1]
                
                l,r = 0, min(i,j)+1
                while l < r:
                    mid = l + (r-l+1) // 2
                    if check(i,j,mid):
                        l = mid
                    else:
                        r = mid-1
                
                res = max(res, l)
        return res

class Solution2:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix matrix
        # time O(m*n*min(m,n)), space O(1)
        m = len(mat)
        n = len(mat[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    mat[i][j] += mat[i-1][j]
                if j > 0:
                    mat[i][j] += mat[i][j-1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i-1][j-1]
                for l in range(1, min(i,j) + 2):
                    s = 0
                    if i - l >= 0:
                        s += mat[i-l][j]
                    if j - l >= 0:
                        s += mat[i][j-l]
                    if i-l >= 0 and j-l >= 0:
                        s -= mat[i-l][j-l]          
                    if mat[i][j] - s <= threshold:
                        res = max(res, l)
        return res
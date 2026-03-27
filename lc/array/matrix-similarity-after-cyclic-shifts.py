class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # time O(m*n), space O(1)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                idx = (j+k) % n if i % 2 else (j-k) % n
                if mat[i][j] != mat[i][idx]:
                    return False
        return True

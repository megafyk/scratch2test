class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # histogram + monotonic stack
        # time O(m*n), space O(n)
        m = len(mat)
        n = len(mat[0])
        height = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            
            st = []
            row_sum = 0
            for j in range(n):
                cnt = 1
                while st and st[-1][0] >= height[j]:
                    prev_h, prev_cnt = st.pop()
                    row_sum -= prev_h * prev_cnt
                    cnt += prev_cnt

                row_sum += height[j] * cnt
                st.append((height[j], cnt))
                res += row_sum 
        return res
                
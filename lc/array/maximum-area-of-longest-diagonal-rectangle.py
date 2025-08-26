class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        mx_diagonal = 0
        for x,y in dimensions:
            diagonal = (x**2 + y**2)
            if diagonal >= mx_diagonal:
                if diagonal == mx_diagonal:
                    res = max(res, x*y)
                else:
                    mx_diagonal = diagonal
                    res = x * y
        return res
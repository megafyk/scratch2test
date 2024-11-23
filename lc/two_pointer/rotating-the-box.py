class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # matrix
        # time O(m*n), space O(m*n)
        m = len(box)
        n = len(box[0])

        for row in box:
            i,j = 0,0
            stones = 0
            while j <= n:
                if j == n or row[j] == "*":
                    for t in range(j-1, i-1, -1):
                        if stones > 0:
                            row[t] = "#"
                            stones -= 1
                        else:
                            row[t] = "."
                    j+=1
                    i=j
                elif row[j] == "#":
                    stones += 1
                    j += 1
                else:
                    j += 1
        rotate = [["*"] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rotate[j][m-1-i] = box[i][j]
        return rotate

    # def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    #     m = len(box)
    #     n = len(box[0])
    #     ans = [['.'] * m for _ in range(n)]
    #     for i in range(m):
    #         k = n - 1
    #         for j in range(n - 1, -1, -1):
    #             if box[i][j] == "*":
    #                 k = j - 1
    #                 ans[j][m - i - 1] = box[i][j]
    #             elif box[i][j] == "#":
    #                 box[i][j], box[i][k] = box[i][k], box[i][j]
    #                 ans[j][m - i - 1], ans[k][m - i - 1] = box[i][j], box[i][k]
    #                 k -= 1

    #     return ans

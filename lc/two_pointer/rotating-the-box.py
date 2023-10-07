from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        ans = [['.'] * m for _ in range(n)]
        for i in range(m):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == "*":
                    k = j - 1
                    ans[j][m - i - 1] = box[i][j]
                elif box[i][j] == "#":
                    box[i][j], box[i][k] = box[i][k], box[i][j]
                    ans[j][m - i - 1], ans[k][m - i - 1] = box[i][j], box[i][k]
                    k -= 1

        return ans


s = Solution()
print(s.rotateTheBox([["#", ".", "#"]]))
print(s.rotateTheBox())

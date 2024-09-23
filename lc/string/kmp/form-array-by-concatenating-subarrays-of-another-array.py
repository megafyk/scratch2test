class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        kmp = []

        for row in groups:
            n = len(row)
            tmp = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and row[i] != row[j]:
                    j = tmp[j-1]
                if row[i] == row[j]:
                    j += 1
                    tmp[i] = j
            kmp.append(tmp)

        n = len(nums)
        j, mat = 0, 0

        for i in range(n):
            
            while j > 0 and groups[mat][j] != nums[i]:
                j = kmp[mat][j-1]
            if groups[mat][j] == nums[i]:
                j += 1
                if j == len(kmp[mat]):
                    j = 0
                    mat += 1
                    if mat == len(kmp):
                        return True
        return False
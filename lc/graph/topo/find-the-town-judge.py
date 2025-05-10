class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # graph
        # time O(N), space O(1)
        ind = [0] * (n+1)
        out = [0] * (n+1)
        for a,b in trust:
            ind[b] += 1
            out[a] += 1

        for i in range(1, n+1):
            if ind[i] == n-1 and out[i] == 0:
                return i
        return -1
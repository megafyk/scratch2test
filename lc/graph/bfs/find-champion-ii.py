class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # bfs topo
        # time O(n), space O(n)
        indegree = [0] * n
        for u,v in edges:
            indegree[v] += 1
        cnt = 0
        t = 0
        for idx, val in enumerate(indegree):
            if val == 0:
                if cnt >0:
                    return -1
                cnt += 1
                t = idx
        return t

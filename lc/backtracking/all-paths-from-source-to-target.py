from collections import defaultdict
class Solution:
    def dfs(self, res, path, gp, visited, src, des):
        if path and path[-1] == des:
            res.append(list(path))
            return

        visited[src] = True
        for node in gp[src]:
            if visited[node]:
                continue
            
            path.append(node)
            self.dfs(res, path, gp, visited, node, des)
            path.pop()
        visited[src] = False

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # complexity: time O(u^v), mem O(n)
        n = len(graph)
        visited = [False] * n
        res = []
        path = [0]
        self.dfs(res, path, graph, visited, 0, n-1)
        return res
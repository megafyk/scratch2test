class Solution:
    def dfs(self, res, path, gp, src, des):

        if path and path[-1] == des:
            res.append(list(path))
            return
        for node in gp[src]:            
            path.append(node)
            self.dfs(res, path, gp, node, des)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # complexity: time O(u^v), mem O(n)
        n = len(graph)
        res = []
        path = [0]
        self.dfs(res, path, graph, 0, n-1)
        return res
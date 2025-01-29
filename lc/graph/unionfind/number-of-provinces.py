class Solution:
    def find(self, cur, par):
        if cur != par[cur]:
            par[cur] = self.find(par[cur], par)
        return par[cur]
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # complexity: time O(n^2), mem O(n) 
        n = len(isConnected)
        par = [i for i in range(n)]
        res = n
        for i in range(n):
            for j in range(i+1, n):
                if not isConnected[i][j]:
                    continue
                p1 = self.find(i, par)
                p2 = self.find(j, par)
                
                if p1 == p2:
                    continue
                res -= 1
                if p1 < p2:
                    par[p2] = p1
                else:
                    par[p1] = p2
        return res


    # def dfs(self, graph, visited, u):
    #     visited.add(u)
    #     n = len(graph)
    #     for i in range(n):
    #         if graph[u][i] and i not in visited:
    #             self.dfs(graph, visited, i)

    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     # complexity O(n^2), mem O(n)
    #     n = len(isConnected)
    #     res = 0
    #     visited = set()
    #     for i in range(n):
    #         if i not in visited:
    #             res += 1
    #             self.dfs(isConnected, visited, i)
    #     return res
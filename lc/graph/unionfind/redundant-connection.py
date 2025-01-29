class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph union-find
        # time O(n), space O(n)
        N = len(edges)
        par = [i for i in range(N+1)]
        # find
        def find(cur):
            if cur != par[cur]:
                cur = find(par[cur])
            return par[cur]
        res = []
        for u,v in edges:
            p1 = find(u)
            p2 = find(v)
            # same root -> cycle 
            if p1 == p2:
                res = [u,v]
                continue
            # union
            if p1 > p2:
                par[p1] = p2 
            else:
                par[p2] = p1
        return res
class Solution:

    def find(self, cur, par):
        if cur != par[cur]:
            cur = self.find(par[cur], par)
        return par[cur]
    
    def disjoinset(self, n, edges):
        # n is number of vertices
        # node -> node edges = [[1,2],[2,3],[3,1]]
        # init parrent root
        par = [i for i in range(n)]

        
        for i, j in edges:
            # find step
            p1 = self.find(i, par)
            p2 = self.find(j, par)
            
            # i,j has same root <=> i,j same set
            if p1 == p2:
                continue

            # union step
            if p1 < p2:
                par[p2] = p1
            else:
                par[p1] = p2
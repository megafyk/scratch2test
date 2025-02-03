class Solution:

    def find(self, cur, par):
        if cur != par[cur]:
            par[cur] = self.find(par[cur], par)
        return par[cur]

    def removeStones(self, stones: List[List[int]]) -> int:
        # use union find ds
        # complexity: time O(n^2), mem O(n)
        n = len(stones)
        par = {}
        for i in range(n):
            s = (stones[i][0], stones[i][1])
            par[s] = s
        for i in range(n-1):
            for j in range(i+1, n):
                stone1, stone2 = (stones[i][0], stones[i][1]), (stones[j][0], stones[j][1])
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    # find
                    p1 = self.find(stone1, par)
                    p2 = self.find(stone2, par)

                    # already in same set
                    if p1 == p2:
                        continue
                    
                    # union 2 nodes
                    if p1[0] > p2[0]:
                        par[p2] = p1
                    else:
                        par[p1] = p2
        res = 0
        for k, v in par.items():
            if k != v:
                res += 1

        return res

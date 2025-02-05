class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, cur):
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur

    def union(self, u1, u2):
        p1 = self.find(u1)
        p2 = self.find(u2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # graph union find -> join idx of 2 account
        # time O(n*e + n*elog(e))
        uf = UnionFind(len(accounts))
        email_acc = {}
        for idx, a in enumerate(accounts):
            for i in range(1, len(a)):
                e = a[i]
                if e in email_acc:
                    uf.union(idx, email_acc[e])
                else:
                    email_acc[e] = idx
                
        email_group = defaultdict(list)
        for e,idx in email_acc.items():
            leader = uf.find(idx)
            email_group[leader].append(e)
        
        res = []
        for idx, emails in email_group.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res
        
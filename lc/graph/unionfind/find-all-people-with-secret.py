from functools import cmp_to_key

class UnionFind:
    def __init__(self, par):
        self.par = par
    
    def find(self, u):
        while self.par[u] != u:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2

class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # graph union find
        # time O(nlogn), space O(n)     
        uf = UnionFind({i:i for i in range(n)})
        meetings.append([0,firstPerson,0])
        meetings = sorted(meetings, key=lambda x: x[2])
        N = len(meetings)
        i = 0
        while i < N:
            cur_time = meetings[i][2]
            group_meetings = []

            participants = set()
            while i < N and meetings[i][2] == cur_time:
                u,v,_ = meetings[i]
                group_meetings.append((u,v))
                participants.add(u)
                participants.add(v)
                i+=1
            
            tmp_uf = UnionFind({p:p for p in participants})
            for u,v in group_meetings:
                tmp_uf.union(u,v)
            
            groups = defaultdict(list)
            for p in participants:
                r = tmp_uf.find(p)
                groups[r].append(p)
            
            for group in groups.values():
                if any(uf.find(p) == 0 for p in group):
                    for p in group:
                        uf.union(p, 0)

        return [i for i in range(n) if uf.find(i) == 0]

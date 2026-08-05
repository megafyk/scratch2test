class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # bfs
        # time O(n), space O(n)
        adj = defaultdict(list)
        for u,v in invocations:
            adj[u].append(v)

        sus = set()
        sus.add(k)
        q = deque([k])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in sus:
                    q.append(v)
                    sus.add(v)
        for u,v in invocations:
            if u not in sus and v in sus:
                return [i for i in range(n)]
        return [u for u in range(n) if u not in sus]

class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        # graph bfs
        # time O(2m+2n+m^2+n^2), space O(m+n)
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def target_nodes(adj, n, depth):
            target = [0] * n
            for i in range(n):
                q = deque([(i, -1)])
                cnt = 0
                cur_depth = 0
                while q:
                    for _ in range(len(q)):
                        u, p = q.popleft()
                        if cur_depth > depth:
                            continue
                        cnt += 1
                        for v in adj[u]:
                            if v != p:
                                q.append((v, u))
                    cur_depth += 1
                target[i] = cnt

            return target

        target1 = target_nodes(adj1, n, k)
        target2 = target_nodes(adj2, m, k - 1)
        t2 = max(target2)
        res = [0] * n
        for i in range(n):
            res[i] = target1[i] + t2
        return res

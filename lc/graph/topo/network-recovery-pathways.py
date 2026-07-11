class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        adj = defaultdict(list)
        if not edges:
            return -1

        costs = set()
        indegree = [0] * n
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                costs.add(cost)
                indegree[v] += 1
        sorted_costs = sorted(list(costs))

        q = deque()
        toposort = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                toposort.append(i)

        while q:
            u = q.popleft()
            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    toposort.append(v)

        def path_exist(lim_edge):
            dp = [inf] * n  # dp[i] => lowest total cost from 0 to i
            dp[0] = 0
            for u in toposort:
                if dp[u] == inf:
                    continue
                for v, c in adj[u]:
                    if c < lim_edge:
                        continue
                    t = dp[u] + c
                    if t < dp[v]:
                        dp[v] = t
            return dp[n - 1] <= k

        l, r = 0, len(sorted_costs) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            lim = sorted_costs[mid]
            if path_exist(lim):
                res = lim
                l = mid + 1
            else:
                r = mid - 1
        return res


class Solution1:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        adj = defaultdict(list)
        if not edges:
            return -1

        costs = set()
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                costs.add(cost)

        sorted_costs = sorted(list(costs))

        def path_exist(lim_edge):
            pq = [(0, 0)]
            dist = [inf] * n
            dist[0] = 0
            while pq:
                cur_cost, u = heappop(pq)
                if u == n - 1:
                    return True
                for v, c in adj[u]:
                    if c >= lim_edge:
                        nw_cost = cur_cost + c
                        if nw_cost <= k and nw_cost < dist[v]:
                            heappush(pq, (nw_cost, v))
                            dist[v] = nw_cost
            return False

        l, r = 0, len(sorted_costs) - 1
        res = -1
        while l < r:
            mid = l + (r - l + 1) // 2
            lim = sorted_costs[mid]
            if path_exist(lim):
                res = lim
                l = mid
            else:
                r = mid - 1
        return res


class Solution2:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        # bfs brute force (mle)
        # time O(n^2), space O(n^2)
        n = len(online)
        adj = defaultdict(list)

        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))

        q = deque()
        q.append((0, 0, inf))
        res = -1
        while q:
            u, cur_cost, mi_edge = q.popleft()
            if u == n - 1:
                res = max(res, mi_edge)
            for v, c in adj[u]:
                nw_cost = cur_cost + c
                if nw_cost <= k:
                    q.append((v, nw_cost, min(c, mi_edge)))
        return res

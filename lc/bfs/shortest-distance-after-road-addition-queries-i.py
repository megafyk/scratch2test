class Solution:

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # bfs
        # time O(n*q), space O(n+q)
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        def distance(src, dst):
            q = deque([(src, 0)])
            visited = set()
            while q:
                u, dis = q.popleft()
                visited.add(u)
                if u == dst: return dis
                for v in graph[u]:
                    if v not in visited:
                        q.append((v, dis + 1))
            return -1

        res = []
        for u, v in queries:
            graph[u].append(v)
            res.append(distance(0, n - 1))

        return res

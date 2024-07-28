from heapq import *


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        # complexity: time O(n + elogn), mem O(n+e)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist1 = [float("inf")] * (n + 1)
        dist2 = [float("inf")] * (n + 1)
        dist1[1] = 0
        freq = [0] * (n + 1)
        pq = []
        heappush(pq, (0, 1))

        while pq:
            time_taken, u = heappop(pq)
            freq[u] += 1

            if freq[u] == 2 and u == n:
                return time_taken
            if (time_taken // change) % 2:
                # time spend when red light in u
                time_taken = change * (time_taken // change + 1) + time
            else:
                # time spend when green light in u
                time_taken += time

            for v in adj[u]:
                if freq[v] == 2:
                    continue
                if time_taken < dist1[v]:
                    dist1[v], dist2[v] = time_taken, dist1[v]
                    heappush(pq, (time_taken, v))
                elif time_taken < dist2[v] and dist1[v] != time_taken:
                    dist2[v] = time_taken
                    heappush(pq, (time_taken, v))
        return 0

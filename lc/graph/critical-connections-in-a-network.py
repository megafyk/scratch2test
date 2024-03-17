from typing import List

# TODO: must do again, hint: https://codeforces.com/blog/entry/71146

class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        # build graph
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovered_at = [-1 for _ in range(n)]
        lowest_reachable = [-1 for _ in range(n)]
        time = 0
        res = []

        def dfs(u, parent_u):
            nonlocal time

            discovered_at[u] = lowest_reachable[u] = (
                time  # set default when a node visisted
            )
            time += 1

            for v in graph[u]:
                # calc discovered_at & lowest_reachable of unvisisted v
                if discovered_at[v] == -1:
                    dfs(v, u)
                    # if u -> v not a back path
                    if lowest_reachable[v] > discovered_at[u]:
                        res.append([u, v])
                    lowest_reachable[u] = min(lowest_reachable[u], lowest_reachable[v])
                elif v != parent_u:  # traverse in 1 direction
                    lowest_reachable[u] = min(
                        lowest_reachable[u], discovered_at[v]
                    )  # farthest descendant discover time

        dfs(0, -1)
        return res

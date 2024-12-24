class Solution:

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # dfs graph
        # time O(m+n), space O(m+n)
        gp1 = defaultdict(list)
        gp2 = defaultdict(list)

        for u,v in edges1:
            gp1[u].append(v)
            gp1[v].append(u)

        for u,v in edges2:
            gp2[u].append(v)
            gp2[v].append(u)

        def diameter(graph, cur, par):
            mx_d = 0
            mx_path = [0,0]
            for v in graph[cur] :
                if v != par:
                    mx_v_d, mx_v_path = diameter(graph, v, cur)
                    mx_d = max(mx_d, mx_v_d)

                    heappush(mx_path, mx_v_path)
                    heappop(mx_path)

            mx_d = max(mx_d, sum(mx_path))
            return mx_d, 1 + max(mx_path)

        d1, _ = diameter(gp1, 0, -1)
        d2, _ = diameter(gp2, 0, -1)

        return max(d1, d2, math.ceil(d1/2) + 1 + math.ceil(d2/2))

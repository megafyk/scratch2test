class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # bfs graph
        # time O(n), space O(n)
        n = len(edges)
        def bfs(node):
            visit = [False] * n
            visit[node] = True
            dist = [-1] * n
            dist[node] = 0
            q = deque([node])
            cur_dist = 0
            while q:
                u = q.popleft()
                v = edges[u]
                if not visit[v] and v != -1:
                    q.append(v)
                    cur_dist += 1
                    dist[v] = cur_dist
                    visit[v] = True
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_dist = sys.maxsize
        res = -1
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                d = max(dist1[i], dist2[i])
                if d < min_dist:
                    res = i
                    min_dist = d
        
        return res
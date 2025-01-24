class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # graph topo sort
        # time O(n), space O(n)
        n = len(graph)
        indegree = [0] * n
        adj = defaultdict(list)
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        safe = [False] * n
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            idx = q.popleft()
            safe[idx] = True
            for v in adj[idx]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return [i for i in range(n) if safe[i]]

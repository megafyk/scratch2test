from collections import deque


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        # topology sort
        # complexity: time O(V+E), mem O(n)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        res = []
        q = deque()
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        for idx, inde in enumerate(indegree):
            if inde == 0:
                q.append(idx)

        while q:
            u = q.popleft()
            res.append(u)

            for v in adj[u]:
                indegree[v] -= 1
                # usually dp go from here
                # ...
                # end
                if indegree[v] == 0:
                    q.append(v)
        return res if len(res) == n else []


# from collections import deque
#
#
# class Solution:
#     def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
#         indegree = [0 for _ in range(numCourses)]
#         graph = [[] for _ in range(numCourses)]
#
#         for i in range(len(pre)):
#             course, precourse = pre[i][0], pre[i][1]
#             graph[precourse].append(course)
#             indegree[course] += 1
#
#         res = []
#         q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
#         while q:
#             v = q.popleft()
#             for u in graph[v]:
#                 indegree[u] -= 1
#                 if indegree[u] == 0:
#                     q.append(u)
#
#             res.append(v)
#
#         return res if len(res) == numCourses else []

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for i in range(len(pre)):
            course, precourse = pre[i][0], pre[i][1]
            graph[precourse].append(course)
            indegree[course] += 1

        res = []
        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        while q:
            v = q.popleft()
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)

            res.append(v)

        return res if len(res) == numCourses else []
